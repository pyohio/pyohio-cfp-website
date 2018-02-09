from django import forms
from symposion.proposals.forms import ProposalMixIn

from .models import ConferenceSpeaker, TalkProposal, TutorialProposal


class ConferenceSpeakerForm(forms.ModelForm):

    class Meta:
        model = ConferenceSpeaker
        exclude = [
            'user',
            'biography_html',
            'experience_html',
            'invite_email',
            'invite_token',
            'annotation',
        ]

    def __init__(self, *a, **k):
        super(ConferenceSpeakerForm, self).__init__(*a, **k)
        self.fields['code_of_conduct'].required = True



class ProposalForm(forms.ModelForm, ProposalMixIn):

    def __init__(self, *a, **k):
        super(ProposalForm, self).__init__(*a, **k)
        self.description_required()
        self.abstract_required()
        self.fields["additional_notes"].help_text = ("Anything else "
            "you'd like the program committee to know when making their "
            "selection. This is not made public. "
            "Edit using "
            "<a href='http://daringfireball.net/projects/markdown/basics' "
            "target='_blank'>Markdown</a>.")

        for field in ("description", "abstract", "additional_notes"):
            self.fields[field].help_text += (" Please do not include "
                "any information that could identify you, as your proposal "
                "will be reviewed anonymously.")


    def clean_description(self):
        value = self.cleaned_data["description"]
        if len(value) > 400:
            raise forms.ValidationError(
                u"The description must be less than 400 characters"
            )
        return value


class TalkProposalForm(ProposalForm):

    class Meta:
        model = TalkProposal
        fields = [
            "title",
            "description",
            "abstract",
            "new_presentation",
            "extended_presentation",
            "additional_notes",
            "extra_av",
            "slides_release",
            "recording_release",
        ]


class TutorialProposalForm(ProposalForm):

    class Meta:
        model = TutorialProposal
        fields = [
            "title",
            "description",
            "abstract",
            "new_presentation",
            "additional_notes",
            "extra_av",
            "prerequisite_setup",
            "participant_limit",
            "slides_release",
            "recording_release",
        ]
