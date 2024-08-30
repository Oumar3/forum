from django.urls import path

app_name = "inseed_apropos"

from . import views

urlpatterns = [
    path("", views.apropos, name="apropos"),
]