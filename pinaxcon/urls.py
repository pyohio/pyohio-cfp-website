import os
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.templatetags.staticfiles import static as _static
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from django.views.static import serve
#from django_nyt.urls import get_pattern as get_nyt_pattern
# from wiki.urls import get_pattern as get_wiki_pattern

from django.contrib import admin

from pinaxcon import views
from pinaxcon.static import serve_index

import symposion.views

URL_PREFIX = settings.URL_PREFIX

original_patterns = [
    url(r"^$", TemplateView.as_view(template_name="static_pages/homepage.html"), name="home"),

    # about
    url(r"^about/keep-in-touch$", TemplateView.as_view(template_name="static_pages/about/keep-in-touch.html"), name="about/keep-in-touch"),
    # TODO:
    # url(r"^about/pyohio$", TemplateView.as_view(template_name="static_pages/about/pyohio.html"), name="about/pyohio"),
    # url(r"^about/columbus$", TemplateView.as_view(template_name="static_pages/about/columbus.html"), name="about/columbus"),
    url(r"^about/team$", TemplateView.as_view(template_name="static_pages/about/team.html"), name="about/team"),
    # rename to about/credits: url(r"^about/colophon$", TemplateView.as_view(template_name="static_pages/about/colophon.html"), name="about/colophon"),
    # Maybe:
    # url(r"^about/transparency$", TemplateView.as_view(template_name="static_pages/about/transparency/transparency.html"), name="about/transparency"),
    # url(r"^about/program-transparency$", TemplateView.as_view(template_name="static_pages/about/transparency/program.html"), name="about/program-transparency"),

    # program
    url(r"^program/events/?$", TemplateView.as_view(template_name="static_pages/program/events.html"), name="program/events"),
    url(r"^events$", RedirectView.as_view(url="program/events")),
    url(r"^program/call-for-proposals$", TemplateView.as_view(template_name="static_pages/program/call_for_proposals.html"), name="program/call-for-proposals"),
    url(r"^program/review-proposals$", TemplateView.as_view(template_name="static_pages/program/review_proposals.html"), name="program/review-proposals"),
    url(r"^program/selection-process$", TemplateView.as_view(template_name="static_pages/program/selection_process.html"), name="program/selection-process"),
    url(r"^cfp$", RedirectView.as_view(url="program/call-for-proposals")),
    url(r"^program/sprints$", TemplateView.as_view(template_name="static_pages/program/sprints_and_receptions.html"), name="about/sprints"),
    url(r"^program/young-coders$", TemplateView.as_view(template_name="static_pages/program/pykids.html"), name="about/pykids"),

    # attend
    # TODO:
     url(r"^attend/register$", TemplateView.as_view(template_name="static_pages/attend/register.html"), name="attend/register"),
    url(r"^attend$", RedirectView.as_view(url="attend/register")),
    # url(r"^registration/register$", views.buy_ticket, name="buy_ticket"),
    url(r"^attend/travel$", TemplateView.as_view(template_name="static_pages/attend/travel.html"), name="attend/travel"),
    url(r"^attend/hotels$", TemplateView.as_view(template_name="static_pages/attend/hotels.html"), name="attend/hotels"),
    url(r"^attend/volunteer$", TemplateView.as_view(template_name="static_pages/attend/volunteer.html"), name="attend/volunteer"),
    # url(r"^attend/tshirt$", TemplateView.as_view(template_name="static_pages/attend/tshirt.html"), name="attend/tshirt"),
    # url(r"^attend/accessibility-and-accommodations$",TemplateView.as_view(template_name="static_pages/attend/accommodations.html"), name="attend/accessibility-and-accommodations"),
    # url(r"^accessibility$", RedirectView.as_view(url="attend/accessibility-and-accommodations")),
    # url(r"^guides$",TemplateView.as_view(template_name="static_pages/attend/guides.html"), name="attend/guides"),
    # url(r"^guide$", RedirectView.as_view(url="guides")),

    # url(r"^emergencies$", TemplateView.as_view(template_name="static_pages/attend/emergencies.html"), name="attend/emergencies"),
    # url(r"^emergency$", RedirectView.as_view(url="emergencies")),
    # url(r"^attend/food$", TemplateView.as_view(template_name="static_pages/attend/food.html"), name="attend/food"),
    # url(r"^food$", RedirectView.as_view(url="attend/food")),
    # url(r"^attend/transit$", TemplateView.as_view(template_name="static_pages/attend/transit.html"), name="attend/transit"),
    # url(r"^transit$", RedirectView.as_view(url="attend/transit")),
    # Maybe:
    # url(r"^attend/business-case$", TemplateView.as_view(template_name="static_pages/attend/business-case.html"), name="attend/business-case"),

    url(r"^code-of-conduct$", TemplateView.as_view(template_name="static_pages/code_of_conduct/code_of_conduct.html"), name="code-of-conduct"),
    url(r"^code-of-conduct/harassment-incidents$", TemplateView.as_view(template_name="static_pages/code_of_conduct/harassment_procedure_attendee.html"), name="code-of-conduct/harassment-incidents"),
    url(r"^code-of-conduct/harassment-staff-procedures$", TemplateView.as_view(template_name="static_pages/code_of_conduct/harassment_procedure_staff.html"), name="code-of-conduct/harassment-staff-procedures"),
    # Maybe:
    # url(r"^terms-and-conditions$", TemplateView.as_view(template_name="static_pages/terms_and_conditions.html"), name="terms-and-conditions"),
    # url(r"^terms$", RedirectView.as_view(url="terms-and-conditions")),

    # sponsor
    url(r"^sponsors/prospectus$", TemplateView.as_view(template_name="static_pages/sponsors/prospectus.html"), name="sponsors/prospectus"),
    url(r"^prospectus.pdf$", RedirectView.as_view(url=_static("assets/PyOhio-2018-Sponsorship-Prospectus.pdf")), name="pyohio-2018-prospectus.pdf"),
    url(r"^sponsors/become-a-sponsor$", TemplateView.as_view(template_name="static_pages/sponsors/become_a_sponsor.html"), name="sponsors/become-a-sponsor"),
    url(r"^sponsors/individual$", TemplateView.as_view(template_name="static_pages/sponsors/individual.html"), name="sponsors/individual"),
    # url(r"^donate$", RedirectView.as_view(url="sponsors/donate")),
    # url(r"^about/donate$", RedirectView.as_view(url="sponsors/donate")),

    # jobs
    url(r"^jobs$", TemplateView.as_view(template_name="static_pages/jobs/job_board.html"), name="jobs"),

    # Django, Symposion, and Registrasion URLs
    url(r"^login$", views.account_login, name="dashboard_login"),
    # Override the default account_login view with one that takes email addys
    url(r"^account/login/$", views.EmailLoginView.as_view(), name="account_login"),
    url(r"^account/signup/$", views.EmailSignupView.as_view(), name="account_signup"),
    url(r"^account/", include("account.urls")),

    url(r"^dashboard/", symposion.views.dashboard, name="dashboard"),

    url(r"^admin/login/", views.EmailLoginView.as_view(), name="admin_login"),
    url(r"^admin/", include(admin.site.urls)),

    url(r"^speaker/", include("symposion.speakers.urls")),
    url(r"^proposals/", include("symposion.proposals.urls")),
    url(r"^sponsors/", include("symposion.sponsorship.urls")),
    url(r"^reviews/", include("symposion.reviews.urls")),
    url(r"^schedule/", include("symposion.schedule.urls")),

    url(r"^teams/", include("symposion.teams.urls")),

    # Demo payment gateway and related features
    url(r"^tickets/payments/", include("registripe.urls")),

    # Required by registrasion
    url(r'^tickets/', include('registrasion.urls')),
    url(r'^nested_admin/', include('nested_admin.urls')),
]


urlpatterns = [
    url(r"^$", RedirectView.as_view(url="%s/" % URL_PREFIX, permanent=False)),
    url(r"^coc/?$", RedirectView.as_view(url="%s/code-of-conduct" % URL_PREFIX, permanent=False)),
    url(r"^code-of-conduct/?$", RedirectView.as_view(url="%s/code-of-conduct" % URL_PREFIX, permanent=False)),
    url(r"^conduct/?$", RedirectView.as_view(url="%s/code-of-conduct" % URL_PREFIX, permanent=False)),
    url(r"^account/login/?$", RedirectView.as_view(url="%s/account/login" % URL_PREFIX, permanent=False)),
    url(r"^details/?$", RedirectView.as_view(url="%s/program/events" % URL_PREFIX, permanent=False)),
    url(r"^register/?$", RedirectView.as_view(url="%s/attend" % URL_PREFIX, permanent=False)),
    url(r"^call-for-proposals/?$", RedirectView.as_view(url="%s/program/call-for-proposals" % URL_PREFIX, permanent=False)),
    url(r"^cfp/?$", RedirectView.as_view(url="%s/program/call-for-proposals" % URL_PREFIX, permanent=False)),
    url(r"^hotel/?$", RedirectView.as_view(url="%s/attend/hotels" % URL_PREFIX, permanent=False)),
    url(r"^schedule/?$", RedirectView.as_view(url="%s/schedule" % URL_PREFIX, permanent=False)),
    url(r"^harassment-incidents-staff/?$", RedirectView.as_view(url="%s/code-of-conduct/harassment-staff-procedures" % URL_PREFIX, permanent=False)),
    url(r"^harassment-incidents/?$", RedirectView.as_view(url="%s/code-of-conduct/harassment-incidents" % URL_PREFIX, permanent=False)),
    url(r"^lightning/?$", RedirectView.as_view(url="%s/program/lightning-talks" % URL_PREFIX, permanent=False)),
    url(r"^sponsors/prospectus/?$", RedirectView.as_view(url="%s/sponsors/prospectus" % URL_PREFIX, permanent=False)),
    url(r"^sprints/?$", RedirectView.as_view(url="%s/program/sprints" % URL_PREFIX, permanent=False)),
    url(r"^volunteer/?$", RedirectView.as_view(url="%s/attend/volunteer" % URL_PREFIX, permanent=False)),
    url(r"^video/?$", RedirectView.as_view(url="https://www.youtube.com/channel/UCYqdrfvhGxNW3vXebypqXoQ", permanent=False)),
    url(r"^review-proposals/?$", RedirectView.as_view(url="%s/program/call-for-proposals/review" % URL_PREFIX, permanent=False)),
    url(r"^$", RedirectView.as_view(url="%s" % URL_PREFIX, permanent=False)),
    url(r'^2017/(?P<path>.*)$', serve_index, {
            'document_root': os.path.join(settings.ARCHIVE_ROOT, '2017'),
        }),
    url(r"^%s/" % URL_PREFIX.lstrip('/'), include(original_patterns)),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

handler500 = views.server_error
