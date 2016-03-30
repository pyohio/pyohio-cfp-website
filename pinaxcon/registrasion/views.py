from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from registrasion import models as rego
from registrasion.controllers.invoice import InvoiceController

import models


def demopay(request, invoice_id, access_code):
    ''' Marks the invoice with the given invoice id as paid.
    '''
    invoice_id = int(invoice_id)
    inv = get_object_or_404(rego.Invoice.objects,pk=invoice_id)

    invoice = InvoiceController(inv)

    if not invoice.can_view(user=request.user, access_code=access_code):
        raise Http404()

    to_invoice = redirect("invoice", invoice.invoice.id, access_code)

    try:
        invoice.validate_allowed_to_pay()  # Verify that we're allowed to do this.
    except ValidationError as ve:
        messages.error(request, ve.message)
        return to_invoice

    # Create the payment object
    models.DemoPayment.objects.create(
        invoice=invoice.invoice,
        reference="Demo payment by user: " + request.user.username,
        amount=invoice.invoice.value,
    )

    invoice.update_status()

    messages.success(request, "This invoice was successfully paid.")

    return to_invoice
