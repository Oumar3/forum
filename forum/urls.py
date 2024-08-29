from django.urls import path

app_name = "forum"

from . import views 

urlpatterns = [
    path('', views.forum_list, name='forum_list'),
    path('discusions_list/<int:forum_id>/', views.discusions_list, name='discusions_list'),
    path('post_list/<int:discusion_id>/', views.post_list, name='post_list'),
    path('add_post/<int:discusion_id>/', views.add_post, name='add_post'),
]