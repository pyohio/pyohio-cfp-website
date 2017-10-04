import models

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

@admin.register(models.AttendeeProfile)
class UserProfileAdmin(admin.ModelAdmin):
    model = models.AttendeeProfile
    list_display = ("name", "company", "name_per_invoice")
