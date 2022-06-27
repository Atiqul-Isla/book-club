from pyexpat import model
from django.forms import ModelForm
from .models import Room
from django import forms 

class roomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['host', 'name', 'description']