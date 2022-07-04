from django.forms import ModelForm 
from django.contrib.auth.forms import AuthenticationForm 
from .models import Room
from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class roomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'description']

        ##Setting widgets to connect django.forms to bootstrap for better styling
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your task name here...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter a brief description of your task here...'}),
        }

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'validate','placeholder': 'name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "password1", "password2")
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

        