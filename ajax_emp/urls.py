from django.urls import path
app_name = 'ajax_emp'
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('office', views.officeCRUD, name="office"),
    path('employee', views.employeeCRUD, name="employee"),
]