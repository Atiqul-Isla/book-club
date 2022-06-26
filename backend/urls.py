from django.contrib import admin
from django.urls import path
from . import views

## Routing urls to different templates
urlpatterns = [
    path('', views.home, name='home'),
    path('create-room', views.createRoom, name='create-room'),
    path('delete-room', views.deleteRoom, name='delete-room')
]