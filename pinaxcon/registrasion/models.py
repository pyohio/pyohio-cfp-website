from django.db import models
from registrasion import models as rego

class AttendeeProfile(rego.AttendeeProfileBase):

    @classmethod
    def name_field(cls):
        ''' This is used to pre-fill the attendee's name from the
        speaker profile. If it's None, that functionality is disabled. '''
        return "name"

    def invoice_recipient(self):
        if self.company:
            base = "\n%(company)s\nAttention: %(name_per_invoice)s"
        else:
            base = "%(name_per_invoice)s"
        return base % self.__dict__

    def save(self):
        if not self.name_per_invoice:
            self.name_per_invoice = self.name
        super(AttendeeProfile, self).save()

    # Things that appear on badge
    name = models.CharField(
        verbose_name="Your name (for your conference nametag)",
        max_length=64,
        help_text="Your name, as you'd like it to appear on your badge. ",
    )

    company = models.CharField(
        max_length=64,
        help_text="The name of your company, as you'd like it on your badge",
        blank=True,
    )
    free_text_1 = models.CharField(
        max_length=64,
        verbose_name="Free text line 1",
        help_text="A line of free text that will appear on your badge. Use "
                  "this for your Twitter handle, IRC nick, your preferred "
                  "pronouns or anything else you'd like people to see on "
                  "your badge.",
        blank=True,
    )
    free_text_2 = models.CharField(
        max_length=64,
        verbose_name="Free text line 2",
        blank=True,
    )

    # Other important Information
    name_per_invoice = models.CharField(
        verbose_name="Your legal name (for invoicing purposes)",
        max_length=64,
        help_text="If your legal name is different to the name on your badge, "
                  "fill this in, and we'll put it on your invoice. Otherwise, "
                  "leave it blank.",
        blank=True,
        )
    of_legal_age = models.BooleanField(
        default=False,
        verbose_name="18+?",
        blank=True,
    )
    dietary_requirements = models.CharField(
        max_length=256,
        blank=True,
    )
    accessibility_requirements = models.CharField(
        max_length=256,
        blank=True,
    )
    gender = models.CharField(
        max_length=64,
        blank=True,
    )


class DemoPayment(rego.PaymentBase):
    ''' A subclass of PaymentBase for use in our demo payments function. '''

    pass  # No custom features here, but yours could be here.
