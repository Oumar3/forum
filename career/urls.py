from django.urls import path
from django.conf import settings
from . import views


app_name = "career"

urlpatterns = [
    path('', views.home, name="career"),
    path('detail/<int:id>', views.detail, name="detail"),
    path('postuler/', views.postuler, name="postuler"),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
    path('register', views.register, name="register"),
]