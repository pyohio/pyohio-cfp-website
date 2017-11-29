from registrasion.models import commerce
from registrasion.controllers.category import CategoryController
from registrasion.controllers.item import ItemController
from registrasion.templatetags import registrasion_tags

from decimal import Decimal
from django import template
from django.conf import settings
from django.db.models import Sum
from urllib import urlencode  # TODO: s/urllib/six.moves.urllib/

register = template.Library()


@register.simple_tag(takes_context=True)
def donation_income(context, invoice):
    ''' Calculates the donation income for a given invoice.

    Returns:
        the donation income.

    '''

    # 15% (FSA) goes to Conservancy; 85% is real goods

    fsa_rate = Decimal("0.85")
    rbi_full_ticket = Decimal("68.00")
    rbi_early_bird_discount = Decimal("-21.35")
    rbi = []

    for line in invoice.lineitem_set.all():
        if line.product.category.name == "Ticket":
            if line.product.name.startswith("Unaffiliated Individual"):
                # Includes full price & discounts
                rbi.append(line.total_price * fsa_rate)
            else:
                if line.total_price > 0:
                    rbi.append(rbi_full_ticket)
                elif line.total_price < 0:
                    rbi.append(rbi_early_bird_discount)
        elif line.product.category.name == "T-Shirt":
            rbi.append(line.total_price * fsa_rate)

    donation = max(Decimal('0'), (invoice.value - sum(rbi)))
    return donation.quantize(Decimal('.01'))


# TODO: include van/de/van der/de la/etc etc etc

@register.simple_tag
def name_split(name, split_characters=None):

    tokens = name.split()
    if split_characters is None or len(name) > split_characters:
        even_split = int((len(tokens) + 1) / 2)  # Round up.
    else:
        even_split = len(tokens)

    return {
        "first" : " ".join(tokens[:even_split]),
        "last" : " ".join(tokens[even_split:]),
    }

@register.simple_tag
def company_split(name):
    f =  name_split(name, 18)
    print f
    return f



CLEARED = set([
    "BeeWare Project",
    "Project Jupyter",
    "PSF Packaging WG / PyCon 2018 Chair",
    "PyCon Ukraine",
    "PyLadies PDX",
    "Recovered Silver",
    "Twisted",
    "@vmbrasseur",
])

@register.simple_tag
def affiliation(ticket, user):
    aff = user.attendee.attendeeprofilebase.attendeeprofile.company
    if "Individual" not in ticket or "Sponsor" in ticket:
        return aff
    elif ticket == "Individual Supporter" and aff in CLEARED:
        return aff
    else:
        return ""


@register.simple_tag(takes_context=True)
def ticket_type(context):

    items = registrasion_tags.items_purchased(context)
    for item in items:
        if item.product.category.name == "Ticket":
            return item.product.name
