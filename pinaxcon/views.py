from django.http import HttpResponseServerError
from django.template import RequestContext
from django.template import Template
from django.template.loader import get_template
from django.views import defaults

def server_error(request, template_name=defaults.ERROR_500_TEMPLATE_NAME):
    t = Template("{%% include '%s' %%}" % template_name)
    return HttpResponseServerError(t.render(RequestContext(request)))
