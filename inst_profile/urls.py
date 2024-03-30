# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('friends/', views.friends, name='friends'),
    path('accept_friend_request/<int:friend_request_id>/', views.accept_friend_request, name='accept_friend_request'),
    path('reject_friend_request/<int:friend_request_id>/', views.reject_friend_request, name='reject_friend_request'),
    path('users/', views.user_list, name='user_list'),
    path('send_friend_request/<int:user_id>/', views.send_friend_request, name='send_friend_request'),
]