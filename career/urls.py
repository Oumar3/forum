from django.urls import path
from django.conf import settings
from . import views


app_name = "career"

urlpatterns = [
    path('', views.home, name="career"),
    path('detail/<int:id>', views.detail, name="detail"),
    
]