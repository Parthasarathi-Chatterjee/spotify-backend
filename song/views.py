from django.shortcuts import render, redirect

from .models import Song, Artist
from .forms import *


def index(request):
    songs = Song.objects.all().order_by('?')[:10]
    artists = Artist.objects.all().order_by('?')[:10]
    # print(artists.values())
    context = {'title': 'Spotify', 'songs': songs, 'artists': artists}
    return render(request, 'index.html', context)


def addArtist(request):
    context = {'title': 'Spotify'}
    return render(request, 'add-artist.html', context)

def uploadArtist(request):
    if request.method == 'POST':
        _mutable = request.POST._mutable
        # set to mutable
        request.POST._mutable = True
        # сhange the values you want
        request.POST['created_by'] = 1
        # set mutable flag back
        request.POST._mutable = _mutable

        form = uploadArtistForm(request.POST, request.FILES)
        if form.is_valid():
            print("YES")
            artistName = request.POST['name']
            checkArtist = Artist.objects.filter(name = artistName)
            if not checkArtist:
                form.save()
        else:
            print("No")
    
    return redirect('add-artist')

def addSong(request):
    songs = Song.objects.all()
    artists = Artist.objects.all()
    context = {'title': 'Spotify', 'songs': songs, 'artists': artists}
    return render(request, 'add-song.html', context)

def uploadSong(request):
    if request.method == 'POST':

        _mutable = request.POST._mutable
        # set to mutable
        request.POST._mutable = True
        # сhange the values you want
        request.POST['created_by'] = 1
        # set mutable flag back
        request.POST._mutable = _mutable

        form = uploadSongForm(request.POST, request.FILES)
        if form.is_valid():
            print("YES")
            songName = request.POST['name']
            checkSong = Song.objects.filter(name=songName)
            if not checkSong:
                form.save()
        else:
            print("No")
    
    return redirect('add-song')