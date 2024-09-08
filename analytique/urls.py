from django.urls import path
app_name = 'analytique'
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('area_chart',views.area_chart,name="area_chart"),
    path('datatable',views.datatable,name="datatable")
]