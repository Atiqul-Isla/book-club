from django.contrib import admin
from django.urls import path
from . import views
from .views import login, landingPage
from django.contrib.auth.views import LogoutView

## Routing urls to different templates
urlpatterns = [
    path('', views.landingPage, name='landing-page'),
    path('log-in', login.as_view(), name='login'),
    path('log-out', LogoutView.as_view(next_page='/'), name='logout'),
    path('home', views.home, name='home'),
    path('create-room', views.createRoom, name='create-room'),
    path('edit-room/<str:key>/', views.updateRoom, name='edit-room'),
    path('delete-room/<str:key>/', views.deleteRoom, name='delete-room'),
   
    # path('create-account', views.createAccount, name='create-account'),
]