from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.

## Modelling a discussion room and all information it should hold
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
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