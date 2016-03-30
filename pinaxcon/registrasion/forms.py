import models

from django import forms

class ProfileForm(forms.ModelForm):
    ''' A form for requesting badge and profile information. '''

    class Meta:
        model = models.AttendeeProfile
        exclude = ['attendee']
