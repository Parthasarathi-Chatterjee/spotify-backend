from django import forms
from .models import *

class uploadArtistForm(forms.ModelForm):
    class Meta():
        model = Artist
        fields = ['name', 'image', 'bio', 'dob', 'created_by']
