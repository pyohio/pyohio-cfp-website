from django import forms
from symposion.proposals.forms import ProposalMixIn

from .models import ConferenceSpeaker, TalkProposal


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
