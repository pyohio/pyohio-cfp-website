from django.conf import settings
from django.http import HttpResponseServerError
from django.shortcuts import render
from django.template import RequestContext
from django.template import Template
from django.template.loader import get_template
from django.views import defaults

from account.forms import LoginEmailForm, LoginUsernameForm, SignupForm

def server_error(request, template_name=defaults.ERROR_500_TEMPLATE_NAME):
    t = Template("{%% include '%s' %%}" % template_name)
    return HttpResponseServerError(t.render(RequestContext(request)))


def account_login(request):

    d = {
        "login_form": LoginUsernameForm(),
        "signup_form": SignupForm(),
        "signup_open": getattr(settings, "ACCOUNT_OPEN_SIGNUP", True),
    }

    print d["signup_open"], settings.ACCOUNT_OPEN_SIGNUP
    return render(request, "account_login.html", d)
