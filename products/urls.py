from django.urls import path
app_name = "products"
from . import views

urlpatterns = [
    path("", views.index, name="index"),      # /products/
    path("add_products/",views.add_products,name="add_products"),
    path("update_products/<int:id>",views.update_products,name="update_products"),    # /products/<int:product_id>/a
    path("delete_products/<int:id>",views.delete_products,name="delete_products"),  # /products/<int:product_id>/a
]