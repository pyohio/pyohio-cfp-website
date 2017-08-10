from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

import symposion.views


urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="static_pages/homepage.html"), name="home"),

    # about
    # TODO add /about
    url(r"^about/north-bay-python$", TemplateView.as_view(template_name="static_pages/about/north-bay-python.html"), name="about/north-bay-python"),
    # TODO add /about/the-mystic
    # TODO add /about/petaluma
    url(r"^about/team$", TemplateView.as_view(template_name="static_pages/about/team.html"), name="about/team"),
    url(r"^about/colophon$", TemplateView.as_view(template_name="static_pages/about/colophon.html"), name="about/colophon"),

    # program
    # TODO add /program
    # TODO add /program/sessions
    # TODO add /program/events
    url(r"^program/call-for-proposals$", TemplateView.as_view(template_name="static_pages/program/call-for-proposals.html"), name="program/call-for-proposals"),
    url(r"^program/selection-process$", TemplateView.as_view(template_name="static_pages/program/selection-process.html"), name="program/selection-process"),

    # attend
    # TODO add /attend
    # TODO add /attend/buy-a-ticket
    # TODO add /attend/volunteer
    # TODO add /attend/financial-assistance
    # TODO add /attend/how-to-pitch-your-manager
    # TODO add /attend/how-to-get-here
    # TODO add /attend/where-to-stay
    url(r"^code-of-conduct$", TemplateView.as_view(template_name="static_pages/code-of-conduct/code-of-conduct.html"), name="code-of-conduct"),
    url(r"^code-of-conduct/harassment-incidents$", TemplateView.as_view(template_name="static_pages/code-of-conduct/harassment-procedure-attendee.html"), name="code-of-conduct/harassment-incidents"),
    url(r"^code-of-conduct/harassment-staff-procedures$", TemplateView.as_view(template_name="static_pages/code-of-conduct/harassment-procedure-staff.html"), name="code-of-conduct/harassment-staff-procedures"),
    url(r"^terms-and-conditions$", TemplateView.as_view(template_name="static_pages/terms-and-conditions.html"), name="terms-and-conditions"),

    # sponsor
    # TODO add /sponsors
    url(r"^sponsors/become-a-sponsor$", TemplateView.as_view(template_name="static_pages/sponsors/become-a-sponsor.html"), name="sponsors/become-a-sponsor"),

    # news
    url(r"^news$", TemplateView.as_view(template_name="static_pages/news.html"), name="news"),

    # Django, Symposion, and Registrasion URLs

    url(r"^admin/", include(admin.site.urls)),

    url(r"^account/", include("account.urls")),

    url(r"^dashboard/", symposion.views.dashboard, name="dashboard"),

    url(r"^speaker/", include("symposion.speakers.urls")),
    url(r"^proposals/", include("symposion.proposals.urls")),
    url(r"^sponsors/", include("symposion.sponsorship.urls")),
    url(r"^reviews/", include("symposion.reviews.urls")),
    url(r"^schedule/", include("symposion.schedule.urls")),

    url(r"^teams/", include("symposion.teams.urls")),

    # Demo payment gateway and related features
    url(r"^register/pinaxcon/", include("pinaxcon.registrasion.urls")),

    # Demo payment gateway and related features
    url(r"^register/payments/", include("registripe.urls")),

    # Required by registrasion
    url(r'^register/', include('registrasion.urls')),
    url(r'^nested_admin/', include('nested_admin.urls')),

    # Catch-all MUST go last.
    #url(r"^", include("pinax.pages.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
