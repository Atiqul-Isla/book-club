from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, redirect
from . import models
from . import forms
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



# Create your views here.

## Class based view that handles user authentication from the LoginView library
class login(LoginView):
    template_name = 'backend/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

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
def deleteRoom(request, key):
    room = models.Room.objects.get(id=key)
    context = {'room':room}
    if request.method == 'POST':
        room.delete()
        return redirect('my-rooms')
    return render(request, 'backend/delete.html', context)

## Class based view to create updateRoom functionality for individual users
class updateRoom(LoginRequiredMixin, UpdateView):
    template_name = 'backend/create.html'
    fields = ['name', 'description']
    model = models.Room
    success_url = reverse_lazy('my-rooms')

    def get_queryset(self, **kwargs):
        return models.Room.objects.filter(id=self.kwargs['pk'])

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super(updateRoom, self).form_valid(form)


