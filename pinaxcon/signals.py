""" Experimantal stuff to provide notifications when certain events happen """

import logging

import keen
import requests

from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from symposion.sponsorship.models import Sponsor

from pinaxcon.proposals.models import TalkProposal, TutorialProposal
from pinaxcon.settings import (
        DEFAULT_HTTP_PROTOCOL,
        SLACK_CHANNEL_PROPOSALS,
        SLACK_CHANNEL_SPONSORS,
        SLACK_WEBHOOK_URL
        )


logger = logging.getLogger(__name__)


def make_slack_payload(text, channel=None):
    payload = {
        'text': text,
        'username': 'PyOhio Website',
        'icon_emoji': ':pyohio:',
    }
    if channel is not None:
        payload['channel'] = channel
    return payload

def post_slack_message(text, channel=None):
    payload = make_slack_payload(text, channel)
    try:
        response = requests.post(SLACK_WEBHOOK_URL, json=payload)
        response.raise_for_status()
    except:
        logger.exception('Failed to post Slack message.')


def send_keen_event(stream, event):
    try:
        keen.add_event(stream, event)
    except:
        raise
        logger.exception('Failed to send keen.io event.')


def get_admin_url(instance):
    try:
        info = (instance._meta.app_label, instance._meta.model_name)
        instance_url = reverse('admin:%s_%s_change' % info, args=(instance.pk,))
        # TODO: Get protocol + hostname from request
        admin_url = instance_url
    except:
        logger.exception('Error getting admin URL')
        admin_url = None
    return admin_url


def save_proposal(sender, instance, **kwargs):
    try:
        if kwargs.get('created') and SLACK_WEBHOOK_URL:
            text = '*New proposal created!*\nKind: {}\nTitle: {}\nAdmin: {}'.format(
                    instance.kind,
                    instance.title,
                    get_admin_url(instance)
                    )
            post_slack_message(text, channel=SLACK_CHANNEL_PROPOSALS)
        if kwargs.get('created'):
            event = {
                    'kind': str(instance.kind.slug),
                    'date': instance.submitted.strftime('%Y-%m-%d'),
                    'id': instance.id,
                    }
            send_keen_event('proposals', event)
    except:
        logger.exception('save_proposal callback failed')


def save_sponsor(sender, instance, **kwargs):
    try:
        if kwargs.get('created') and SLACK_WEBHOOK_URL:
            text = ':money_with_wings: *New sponsor application!:*\n Name: {}\nLevel: {}\n Contact: "{}" <{}>\nAdmin: {}\nCreated by: {}'.format(
                    instance.name,
                    instance.level,
                    instance.contact_name,
                    instance.contact_email,
                    get_admin_url(instance),
                    instance.applicant
                    )
            post_slack_message(text, channel=SLACK_CHANNEL_SPONSORS)
    except:
        logger.exception('save_sponsor callback failed')

post_save.connect(save_proposal, sender=TalkProposal)
post_save.connect(save_proposal, sender=TutorialProposal)
post_save.connect(save_sponsor, sender=Sponsor)
