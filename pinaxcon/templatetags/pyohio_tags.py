from django import template
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.safestring import mark_safe
from pinaxcon.proposals.models import ConferenceSpeaker

register = template.Library()

@register.simple_tag
def user_photo(username):
    user = User.objects.get(username=username)
    speaker = ConferenceSpeaker.objects.get(user=user)
    return speaker.photo

@register.simple_tag
def user_bio(username):
    user = User.objects.get(username=username)
    speaker = ConferenceSpeaker.objects.get(user=user)
    return speaker.biography_html

def make_bio_html(username):
    user = User.objects.get(username=username)
    speaker = ConferenceSpeaker.objects.get(user=user)
    html = """<p><img src="{0}" alt="{1}" class="team-headshot">{2}</p>"""
    if speaker.twitter_username:
        twitter_username = speaker.twitter_username.lstrip('@')
        html += """<p><a class="twitter-follow-button" data-show-count="false" href="https://twitter.com/{0}">@{0}</a>""".format(twitter_username)
    if speaker.photo.name:
        photo_url = staticfiles_storage.url(speaker.photo.name)
    else:
        photo_url = staticfiles_storage.url('/images/blank-profile-photo.png')
    return html.format(photo_url, speaker.name, speaker.biography_html)

@register.simple_tag
def user_bio_block(username):
    try:
        html = make_bio_html(username)
    except:
        html = '<p class="bio-block"></p>'
    return mark_safe(html)

