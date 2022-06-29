from django.contrib import admin
from django.urls import path
from . import views
from .views import login, myRooms, createRoom, updateRoom, home
from django.contrib.auth.views import LogoutView

## Routing urls to different templates
urlpatterns = [
    path('', views.landingPage, name='landing-page'),
    path('log-in', login.as_view(), name='login'),
    path('log-out', LogoutView.as_view(next_page='/'), name='logout'),
    path('home', home.as_view(), name='home'),
    path('my-rooms', myRooms.as_view(), name='my-rooms'),
    path('create-room', createRoom.as_view(), name='create-room'),
    path(r'^edit-room/(?P<pk>\d+)/$', updateRoom.as_view(), name='edit-room'),
    path('delete-room/<str:key>/', views.deleteRoom, name='delete-room'),
   
    # path('create-account', views.createAccount, name='create-account'),
]