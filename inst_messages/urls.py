from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name="chat"),
    path('send_message', views.send_message, name="send_message"),
    path('individual_chat/<user_id>', views.individual_chat, name="individual_chat"),
    path('create_group', views.create_group, name="create_group")
]