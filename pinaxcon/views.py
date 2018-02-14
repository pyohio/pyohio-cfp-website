import uuid

from collections import OrderedDict
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseServerError
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.template import Template
from django.template.loader import get_template
from django.views import defaults

from account.forms import LoginEmailForm, LoginUsernameForm, SignupForm
from account.views import LoginView, SignupView

def server_error(request, template_name=defaults.ERROR_500_TEMPLATE_NAME):
    t = Template("{%% include '%s' %%}" % template_name)
    return HttpResponseServerError(t.render(RequestContext(request)))


class SignupEmailForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(SignupEmailForm, self).__init__(*args, **kwargs)
        self.fields.pop('username')
        email = self.fields.pop('email')
        original_fields = self.fields
        self.fields = OrderedDict({'email': email})
        self.fields.update(original_fields)


def account_login(request):

    d = {
        "login_form": LoginEmailForm(),
        "signup_form": SignupEmailForm(),
        "signup_open": getattr(settings, "ACCOUNT_OPEN_SIGNUP", True),
    }

    print d["signup_open"], settings.ACCOUNT_OPEN_SIGNUP
    return render(request, "account_login.html", d)

class EmailSignupView(SignupView):
    form_class = SignupEmailForm
    identifier_field = 'email'
    def generate_username(self, form):
        return str(uuid.uuid4())

class EmailLoginView(LoginView):
    form_class = LoginEmailForm


def buy_ticket(request):

    print(dir(request.user))
    if not request.user.is_authenticated():
        messages.warning(request,
            '''To buy a ticket, either create an account, or log in.
            Attendees should fill out their own registration.
            You will receive a payment link that you can pass to accounts
            staff, if required. ''')

    return redirect("/dashboard")


