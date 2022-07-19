from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


# Create your models here.

##Modelling a Books table and all information it should hold
class Book(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Book Name', max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    image = models.ImageField(height_field=None, width_field=None, max_length=255)

    ## Stringifying name of the book
    def __str__(self):
        return(self.name)

## Modelling a discussion room and all information it should hold
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField('Topic Name', max_length=255)
    description = models.TextField(null=True)
    date_created = models.DateTimeField(default=datetime.datetime.now)

    ## Stringifying name of the host
    def __str__(self):
        return(self.host)

    ## Stringifying name of the discussion room
    def __str__(self):
        return(self.name)

    
     ## Handeling the ordering of how the items are shown
    class Meta:
        ordering = ['-date_created',] 

## Creating a message model to store message data

class Message(models.Model):
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return(self.message)