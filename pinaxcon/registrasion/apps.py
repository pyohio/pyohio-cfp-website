from __future__ import unicode_literals
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class RegistrasionConfig(AppConfig):
    name = "pinaxcon.registrasion"
    label = "pinaxcon_registrasion"
    verbose_name = _("Pinaxcon Registrasion")
