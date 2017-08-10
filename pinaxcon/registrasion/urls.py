from django.conf.urls import url

import views

urlpatterns = [
    url(r"^demopay/([0-9]+)/([A-Z0-9]+)$", views.demopay, name="demopay"),
]
