from django.urls import path

app_name = 'List_product'

from . import views

urlpatterns = [ 
    path("list_products/",views.list_products,name="list_products"),
]