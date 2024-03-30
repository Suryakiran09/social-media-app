from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('comment/<post_id>', views.create_comment, name="create_comment")
]