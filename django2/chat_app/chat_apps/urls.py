from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room>/', views.chat_site, name='chat_site' ),
    path('create_room', views.create_room, name='create_room'),
    path('<str:room>/send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name="getMessages")

]
