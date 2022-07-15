from unicodedata import name
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
    rating = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

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