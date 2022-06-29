from django.forms import ModelForm
from .models import Room
from django import forms 

class roomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'description']

        ##Setting widgets to connect django.forms to bootstrap for better styling
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your task name here...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter a brief description of your task here...'}),
        }

       