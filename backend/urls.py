from django.contrib import admin
from django.urls import path
from . import views

## Routing urls to different templates
urlpatterns = [
    path('', views.home, name='home'),
    path('create-room', views.createRoom, name='create-room'),
    path('edit-room/<str:key>/', views.updateRoom, name='edit-room'),
    path('delete-room/<str:key>/', views.deleteRoom, name='delete-room')
]