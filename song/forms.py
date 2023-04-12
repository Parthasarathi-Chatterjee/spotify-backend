from django import forms
from .models import *
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class uploadSongForm(forms.ModelForm):
    class Meta():
        model = Song
        fields = ['name', 'dateOfRelease', 'image', 'file', 'artist', 'created_by']

class uploadRatingForm(forms.ModelForm):
    class Meta():
        model = Rating
        fields = ['user', 'song', 'rating']

