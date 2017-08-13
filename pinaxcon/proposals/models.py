from django.db import models
from django.utils.translation import ugettext_lazy as _

from symposion.markdown_parser import parse
from symposion.proposals.models import ProposalBase
from symposion.speakers.models import SpeakerBase



class ConferenceSpeaker(SpeakerBase):

    def clean_twitter_username(self):
        value = self.twitter_username
        if value.startswith("@"):
            value = value[1:]
        return value

    def save(self, *args, **kwargs):
        self.experience_html = parse(self.experience)
        self.twitter_username = self.clean_twitter_username()
        return super(ConferenceSpeaker, self).save(*args, **kwargs)

    twitter_username = models.CharField(
        max_length=15,
        blank=True,
        help_text=_(u"Your Twitter account")
    )

    first_time = models.BooleanField(
        blank=True,
        verbose_name=_("First-time speaker?"),
        help_text=_("Check this field if this is your first time speaking "
                    "at a technical conference."),
        )

    experience = models.TextField(blank=True, help_text=_
        ("List any past speaking experience you have. This can include "
         "user groups, meetups, or presentations at work or school.  Edit "
         "using <a href='http://warpedvisions.org/projects/"
         "markdown-cheat-sheet/target='_blank'>"
         "Markdown</a>."),
         verbose_name=_("Past speaking experience"),
    )
    experience_html = models.TextField(blank=True)

    travel_assistance = models.BooleanField(
        blank=True,
        verbose_name=_("Travel assistance required?"),
        help_text=_("Check this field if you require travel assistance to get "
                    "to North Bay Python in Petaluma, California."),
    )

    lodging_assistance = models.BooleanField(
        blank=True,
        verbose_name=_("Lodging assistance required?"),
        help_text=_("Check this field if you require lodging assistance in "
                    "Petaluma, California during North Bay Python."),
    )

    home_city = models.CharField(
        blank=True,
        max_length=127,
        help_text=_("Which city (and state, and country) will you be "
                    "traveling from to get to North Bay Python?"),
    )

    minority_group = models.CharField(blank=True, max_length=256,
        verbose_name=_("Diversity statement"),
        help_text=_("If you are a member of one or more groups that are "
                    "under-represented in the tech industry, you may list "
                    "these here. Your response is optional."),
    )

    code_of_conduct = models.BooleanField(
        help_text=_("I have read and, in the event that my proposal is "
                    "accepted, agree that I will comply with the "
                    "<a href='/code-of-conduct'>Code of Conduct</a>."),
    )


class Proposal(ProposalBase):

    AUDIENCE_LEVEL_NOVICE = 1
    AUDIENCE_LEVEL_EXPERIENCED = 2
    AUDIENCE_LEVEL_INTERMEDIATE = 3

    AUDIENCE_LEVELS = [
        (AUDIENCE_LEVEL_NOVICE, "Novice"),
        (AUDIENCE_LEVEL_INTERMEDIATE, "Intermediate"),
        (AUDIENCE_LEVEL_EXPERIENCED, "Experienced"),
    ]

    audience_level = models.IntegerField(choices=AUDIENCE_LEVELS)

    recording_release = models.BooleanField(
        default=True,
        help_text="By submitting your proposal, you agree to give permission to the conference organizers to record, edit, and release audio and/or video of your presentation. If you do not agree to this, please uncheck this box."
    )

    class Meta:
        abstract = True


class TalkProposal(Proposal):

    class Meta:
        verbose_name = "talk proposal"
