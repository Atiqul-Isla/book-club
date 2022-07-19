from django.contrib import admin
from django.urls import path
from . import views
from .views import MyBooks, Register, loginPage, myRooms, createRoom, updateRoom, home, RegisterBook, ChatRoom
from django.contrib.auth.views import LogoutView
from .forms import CustomAuthForm

## Routing urls to different templates
urlpatterns = [
    path('landing-page', views.landingPage, name='landing-page'),
    path('log-in', loginPage.as_view(), name='login', kwargs={"authentication_form":CustomAuthForm}),
    path('log-out', LogoutView.as_view(next_page='/'), name='logout'),
    path('register', Register.as_view(), name='register'),
    path('', home.as_view(), name='home'),
    path('my-rooms', myRooms.as_view(), name='my-rooms'),
    path('create-room', createRoom.as_view(), name='create-room'),
    path('edit-room/<str:pk>/', updateRoom.as_view(), name='edit-room'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete-room'),
    path('delete-book/<str:pk>/', views.DeleteBook, name='delete-book'),
    path('chat-room/<str:pk>/', ChatRoom.as_view(), name='chat-room'),
    # path('chat-room/<str:pk>/', views.ChatRoom, name='chat-room'),
    path('register-book', RegisterBook.as_view(), name='register-book'),
    path('my-books', MyBooks.as_view(), name='my-books'),
]