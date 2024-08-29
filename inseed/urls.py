from django.urls import path
app_name = "inseed"

from . import views

urlpatterns = [
    path('',views.inseed,name="inseed"),
]