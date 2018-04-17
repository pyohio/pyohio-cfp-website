from django import template
from django.conf import settings
from django.contrib.auth.models import User
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
