from django.shortcuts import render, redirect
from django.http import request
from . import models
from . import forms

# Create your views here.

## Function based view that loads in the home page which displays all active discussion rooms
def home(request):
    rooms = models.Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'backend/home.html', context)

## Creating a function that creates new discussion room using POST request
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
def deleteRoom(request, key):
    room = models.Room.objects.get(id=key)
    context = {'room':room}
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'backend/delete.html', context)

## Creating a function that updates existing discussion rooms using POST request
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