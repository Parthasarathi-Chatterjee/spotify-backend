from django import forms
from .models import *
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class uploadArtistForm(forms.ModelForm):
    class Meta():
        model = Artist
        fields = ['name', 'bio', 'dob', 'created_by']

class uploadSongForm(forms.ModelForm):
    class Meta():
        model = Song
        fields = ['name', 'dateOfRelease', 'cover', 'artist', 'created_by']

class uploadRatingForm(forms.ModelForm):
    class Meta():
        model = Rating
        fields = ['user', 'song', 'rating']

