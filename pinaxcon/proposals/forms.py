from django import forms

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



class ProposalForm(forms.ModelForm):

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
            "audience_level",
            "description",
            "abstract",
            "additional_notes",
            "recording_release",
        ]
