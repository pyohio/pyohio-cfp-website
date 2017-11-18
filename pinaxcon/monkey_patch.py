from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from functools import wraps


class MonkeyPatchMiddleware(object):
    ''' Ensures that our monkey patching only gets called after it is safe to do so.'''

    def process_request(self, request):
        do_monkey_patch()


def do_monkey_patch():
    patch_stripe_card_defaults()
    patch_conference_schedule()

    # Remove this function from existence
    global do_monkey_patch
    do_monkey_patch = lambda: None


def patch_stripe_card_defaults():
    from pinax.stripe.actions import sources
    from collections import defaultdict

    old_sync_card = sources.sync_card

    @wraps(old_sync_card)
    def sync_card(customer, source):
        d = defaultdict(str)
        d.update(source)
        return old_sync_card(customer, d)

    sources.sync_card = sync_card


def patch_conference_schedule():
    from symposion.schedule import views as sv
    from symposion.schedule import models as sm

    old_schedule_json = sv._schedule_json

    @wraps(old_schedule_json)
    def schedule_json(request):
        schedule = old_schedule_json(request)

        for slot_data in schedule:
            slot = sm.Slot.objects.get(id=slot_data["conf_key"])
            presentation = slot.content
            if presentation is not None:
                update_presentation(request, slot_data, presentation)
            elif slot.kind.label.lower() == "keynote":
                update_keynote(request, slot_data)
            elif slot.kind.label.lower() == "housekeeping":
                update_housekeeping(request, slot_data)
            else:
                pass

        return schedule

    def update_presentation(request, slot_data, presentation):
        try:
            slot_data["reviewers"] = (
                presentation.speaker.conferencespeaker.reviewer
                if request.user.is_staff else ["redacted"]
            )
            slot_data["license"] = "CC BY-SA"
            slot_data["released"] = presentation.proposal_base.talkproposal.recording_release
            slot_data["twitter_id"] = presentation.speaker.conferencespeaker.twitter_username
        except Exception as e:
            print e

    def update_keynote(request, slot_data):
        keynotes = {
            "Brandon Rhodes": (User.objects.get(username="brandon").email, "brandon_rhodes"),
            "Carina C. Zona": (User.objects.get(username="cczona").email, "cczona"),
        }
        for speaker, values in keynotes.items():
            print speaker
            if speaker in slot_data["name"]:
                author_name = speaker
                author_email, author_twitter_id = values

        slot_data["name"] = "Keynote"
        slot_data["authors"] = [author_name]
        slot_data["contact"] = [
            author_email
        ] if request.user.is_staff else ["redacted"]
        slot_data["abstract"] = "Keynote presentation from North Bay Python 2017 by " + author_name
        slot_data["description"] = "Keynote presentation from North Bay Python 2017 by " + author_name
        slot_data["conf_url"] = "https://2017.northbaypython.org"
        slot_data["cancelled"] = False
        slot_data["reviewers"] = ""
        slot_data["license"] = "CC BY-SA"
        slot_data["twitter_id"] = author_twitter_id
        slot_data["released"] = True

    def update_housekeeping(request, slot_data):
        slot_data["contact"] = [
            "spam@northbaypython.org"
        ] if request.user.is_staff else ["redacted"]


    sv._schedule_json = schedule_json
