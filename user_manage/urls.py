from django.urls import path
app_name = "user_manage"

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # path('uniquedb/<int:id>',views.uniquedb,name='uniquedb'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register_view, name="register"),
    path('hello/', views.hello_view, name="hello"),
]
