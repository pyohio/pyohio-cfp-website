from registrasion.models import commerce
from registrasion.controllers.category import CategoryController
from registrasion.controllers.item import ItemController

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

    donation = (invoice.value - sum(rbi))
    return donation.quantize(Decimal('.01'))
