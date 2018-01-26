from django.conf import settings

def site_settings(request):
    return {
        'CONFERENCE_YEAR': settings.CONFERENCE_YEAR,
        'URL_PREFIX': settings.URL_PREFIX,
    }
