from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('login', views.user_login, name="login"),
    path('register', views.registration, name="registration"),
    path('logout', views.user_logout, name="logout"),
]
