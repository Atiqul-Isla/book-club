## Django.views.generic libraries for CRUD functionality
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic.detail import DetailView
from django.views import View

## Functins that render views and redirect users
from django.shortcuts import render, redirect, get_object_or_404

## Importing personally created models and forms
from . import models
from . import forms

## Djang.urls for redirecting
from django.urls import reverse_lazy, reverse

## Django.contrib.auth libraries for user authentication
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login





# Create your views here.

## Class based view that handles user authentication from the LoginView library
class loginPage(LoginView):
    template_name = 'backend/login.html'
    fields = '__all__'
    form_class = forms.CustomAuthForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

class Register(FormView):
    template_name = 'backend/register.html'
    form_class = forms.RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)


## Function based view for a landing page that all non logged in users are directed to
def landingPage(request):
    return render(request, 'backend/landing-page.html')
    


## Class based view to display the list of active discussion room regardless of the user
## Below is a python decorator to restrict pages that require the user to login, it is used in many views below
class home(LoginRequiredMixin, ListView):
    template_name = 'backend/home.html'
    model = models.Room 
    context_object_name = 'rooms'

## Class based view used in order to get context data in which the rooms model is filtered by the user
## LoginRequiredMixin serves the same purpose as the @login_required decorator()
class myRooms(LoginRequiredMixin, ListView):
    template_name = 'backend/my-rooms.html'
    model = models.Room 
    context_object_name = 'rooms'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms']= context['rooms'].filter(host=self.request.user)
        return context

## Class based view that takes the roomForm and uses POST requests. This class also hasa  function that determines which user is creating the form
class createRoom(LoginRequiredMixin, CreateView):
    template_name = 'backend/create.html'
    form_class = forms.roomForm
    success_url = reverse_lazy('home')
    form = models.Room
    def form_valid(self, form):
        form.instance.host = self.request.user
        return super(createRoom, self).form_valid(form)



## Creating a function that deletes existing discussion rooms using POST request
@login_required()
def deleteRoom(request, pk):
    room = models.Room.objects.get(id=pk)
    context = {'room':room}
    if request.method == 'POST':
        room.delete()
        return redirect('my-rooms')
    return render(request, 'backend/delete.html', context)

## Class based view to create updateRoom functionality for individual users
class updateRoom(LoginRequiredMixin, UpdateView):
    template_name = 'backend/create.html'
    form_class = forms.roomForm
    form = models.Room
    success_url = reverse_lazy('my-rooms')

    def get_queryset(self, **kwargs):
        return models.Room.objects.filter(id=self.kwargs['pk'])

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super(updateRoom, self).form_valid(form)

# @login_required()
# def ChatRoom(request, pk):
#     return render(request, 'backend/lobby.html', {'pk':pk})


class ChatRoom(LoginRequiredMixin, View):
    def get(self, request, pk):
        room = models.Room.objects.filter(id=pk).first()
        chats = []

        if room:
            chats = models.Message.objects.filter(room=room)
        else:
            room = models.Room(id=pk)
            room.save()

        return render(request, 'backend/lobby.html', {'pk':pk, 'chats': chats})

class RegisterBook(LoginRequiredMixin, CreateView):
    template_name = 'backend/create.html'
    form_class = forms.RegisterBookForm
    success_url = reverse_lazy('home')
    form = models.Book
    def form_valid(self, form):
        form.instance.host = self.request.user
        return super(RegisterBook, self).form_valid(form)

class MyBooks(LoginRequiredMixin, ListView):
    template_name = 'backend/my-books.html'
    model = models.Book
    context_object_name = 'books'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['books']= context['books'].filter(host=self.request.user)
        return context

@login_required()
def DeleteBook(request, pk):
    book = models.Book.objects.get(id=pk)
    context = {'book':book}
    if request.method == 'POST':
        book.delete()
        return redirect('my-books')
    return render(request, 'backend/delete.html', context)

