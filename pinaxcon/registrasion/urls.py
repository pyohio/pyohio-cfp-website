from django.conf.urls import url, patterns

import views

urlpatterns = patterns(
    "pinaxcon.registrasion.views",
    url(r"^demopay/([0-9]+)/([A-Z0-9]+)$", views.demopay, name="demopay"),
)
