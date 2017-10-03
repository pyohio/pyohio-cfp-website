from django.core.exceptions import ValidationError
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django_countries.fields import CountryField
from registrasion import models as rego


class AttendeeProfile(rego.AttendeeProfileBase):

    @classmethod
    def name_field(cls):
        ''' This is used to pre-fill the attendee's name from the
        speaker profile. If it's None, that functionality is disabled. '''
        return "name"

    def invoice_recipient(self):

        lines = [
            self.name_per_invoice,
        ]

        if self.company:
            lines.append("C/- " + self.company)

        if self.address_line_1:
            lines.append(self.address_line_1)

        if self.address_line_2:
            lines.append(self.address_line_2)

        if self.address_suburb or self.address_postcode:
            lines.append("%s %s" % (
                self.address_suburb or "",
                self.address_postcode or "",
            ))

        if self.state:
            lines.append(self.state)

        if self.country:
            lines.append(self.country.name)

        return "\n".join(unicode(line) for line in lines)

    def clean(self):
        errors = []
        if self.country == "US" and not self.state:
            errors.append(
                ("state", "US-based attendees must list their state"),
            )

        if self.address_line_2 and not self.address_line_1:
            errors.append((
                "address_line_1",
                "Please fill in line 1 before filling line 2",
            ))

        if errors:
            raise ValidationError(dict(errors))

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
        help_text="The name of your company, as you'd like it on your badge and receipt",
        blank=True,
    )

    name_per_invoice = models.CharField(
        verbose_name="Your legal name (for your receipt)",
        max_length=256,
        help_text="If your legal name is different to the name on your badge, "
                  "fill this in, and we'll put it on your receipt. Otherwise, "
                  "leave it blank.",
        blank=True,
        )

    address_line_1 = models.CharField(
        verbose_name="Address line 1",
        help_text="This address, if provided, will appear on your receipt.",
        max_length=1024,
        blank=True,
    )
    address_line_2 = models.CharField(
        verbose_name="Address line 2",
        max_length=1024,
        blank=True,
    )
    address_suburb = models.CharField(
        verbose_name="City/Town/Suburb",
        max_length=1024,
        blank=True,
    )
    address_postcode = models.CharField(
        verbose_name="Postal/Zip code",
        max_length=1024,
        blank=True,
    )
    country = CountryField(
        default="US",
    )
    state = models.CharField(
        max_length=256,
        verbose_name="State/Territory/Province",
        blank=True,
    )

    dietary_restrictions = models.CharField(
        verbose_name="Food allergies, intolerances, or dietary restrictions",
        max_length=256,
        blank=True,
    )
    accessibility_requirements = models.CharField(
        verbose_name="Accessibility-related requirements",
        max_length=256,
        blank=True,
    )
    gender = models.CharField(
        help_text="Gender data will only be used for demographic purposes.",
        max_length=64,
        blank=True,
    )

    newsletter = models.BooleanField(
        verbose_name="Subscribe to North Bay Python newsletter",
        help_text="Select to be subscribed to the low-volume North Bay Python "
                  "announcements newsletter",
        blank=True,
    )
