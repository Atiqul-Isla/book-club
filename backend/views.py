from django.shortcuts import render
from django.http import request
from . import models

# Create your views here.

## Function based view that loads in the home page which displays all active discussion rooms
def home(request):
    rooms = models.Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'backend/home.html', context)

def createRoom(request):
    rooms = models.Room.objects.all()
    context = {}
    return render(request, 'backend/create.html', context)

def deleteRoom(request):
    rooms = models.Room.objects.all()
    context = {}
    return render(request, 'backend/delete.html', context)