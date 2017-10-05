from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from functools import wraps


class MonkeyPatchMiddleware(object):
    ''' Ensures that our monkey patching only gets called after it is safe to do so.'''

    def process_request(self, request):
        do_monkey_patch()


def do_monkey_patch():
    patch_stripe_card_defaults()

    # Remove this function from existence
    global do_monkey_patch
    do_monkey_patch = lambda: None


def patch_stripe_card_defaults():
    from pinax.stripe.actions import sources
    from collections import defaultdict

    old_sync_card = sources.sync_card

    def sync_card(customer, source):
        d = defaultdict(str)
        d.update(source)
        return old_sync_card(customer, d)

    sources.sync_card = sync_card
