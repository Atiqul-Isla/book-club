from django.shortcuts import render, redirect
from . import models
from . import forms
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
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
    


## Function based view that loads in the home page which displays all active discussion rooms
## Below is a python decorator to restrict pages that require the user to login, it is used in many views below
@login_required()
def home(request):
    rooms = models.Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'backend/home.html', context)

## Creating a function that creates new discussion room using POST request
@login_required()
def createRoom(request):
    form = forms.roomForm()
    context = {'form':form}
    if request.method == 'POST':
        form = forms.roomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'backend/create.html', context)

## Creating a function that deletes existing discussion rooms using POST request
@login_required()
def deleteRoom(request, key):
    room = models.Room.objects.get(id=key)
    context = {'room':room}
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'backend/delete.html', context)

## Creating a function that updates existing discussion rooms using POST request
@login_required()
def updateRoom(request, key):
    room = models.Room.objects.get(id=key)
    form = forms.roomForm(instance=room)
    context = {'form': form}
    if request.method == 'POST':
        form = forms.roomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request, 'backend/create.html', context)

