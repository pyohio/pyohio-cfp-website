from django.contrib import admin

from .models import ConferenceSpeakerOrganizerRoles, OrganizerRole, TalkProposal, TutorialProposal


admin.site.register(TalkProposal)
admin.site.register(TutorialProposal)
admin.site.register(ConferenceSpeakerOrganizerRoles)
admin.site.register(OrganizerRole)