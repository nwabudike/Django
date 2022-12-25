from django.contrib import admin
from django.urls import path, include
from .views import register_user

urlpatterns = [
    path('register/', register_user.as_view(), name='register')
]
