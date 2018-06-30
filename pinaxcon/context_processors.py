from django.conf import settings

def site_settings(request):
    return {
        'CONFERENCE_YEAR': settings.CONFERENCE_YEAR,
        'URL_PREFIX': settings.URL_PREFIX,
    }

def template_cache_ttls(request):
    try:
        ttl =  int(settings.SCHEDULE_CACHE_TTL)
    except:
        ttl = 300
    return {
            'schedule_cache_ttl': ttl,
            }
