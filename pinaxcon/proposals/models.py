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
        default=False,
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
        default=False,
        verbose_name=_("Travel assistance required?"),
        help_text=_("Check this field if you require travel assistance to get "
                    "to North Bay Python in Petaluma, California."),
    )

    lodging_assistance = models.BooleanField(
        blank=True,
        default=False,
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
        default=False,
        help_text=_("I have read and, in the event that my proposal is "
                    "accepted, agree that I will comply with the "
                    "<a href='/code-of-conduct'>Code of Conduct</a>."),
    )


class Proposal(ProposalBase):

    extended_presentation = models.BooleanField(
        default=False,
        verbose_name=_("Optionally consider this proposal for a 45-minute "
                       "slot"),
        help_text=_("Most talks at North Bay Python go for 30 minutes. We "
                    "have some openings for 45-minute talks. If you check this "
                    "field, please explain in your additional notes how you "
                    "would use the extra 15 minutes."),
    )
    extra_av = models.TextField(
        blank=True,
        verbose_name=_("Extra tech and A/V requirements"),
        help_text=_("We will provide you with a projector with HDMI "
                    "connection, an audio connection, and one microphone per "
                    "speaker. If you need anything more than this to present "
                    "this talk, please list them here."),
    )
    new_presentation = models.BooleanField(
        default=False,
        verbose_name=_("This is a new presentation"),
        help_text=_("Check this box if North Bay Python will be the first "
                    "time this talk is presented at a technical conference."),
    )
    slides_release = models.BooleanField(
        default=True,
        help_text=_("I authorize North Bay Python to release a copy of my "
                    "slides and related materials under the Creative Commons "
                    "Attribution-ShareAlike 3.0 United States licence, and "
                    "certify that I have the authority to do so."),
    )
    recording_release = models.BooleanField(
        default=True,
        help_text=_("I authorize North Bay Python to release a recording of "
                    "my talk under the Creative Commons "
                    "Attribution-ShareAlike 3.0 United States licence."),

    )

    class Meta:
        abstract = True


class TalkProposal(Proposal):

    class Meta:
        verbose_name = "talk proposal"
