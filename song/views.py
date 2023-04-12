from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Song
from .forms import *

from song.serializers import SongSerializer

def index(request):
    songs = Song.objects.all().order_by('?')[:10]
    # artists = Artist.objects.all().order_by('?')[:10]
    # print(artists.values())
    context = {'title': 'Spotify', 'songs': songs}
    return render(request, 'index.html', context)

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

class SongView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            song = Song.objects.all()
        except:
            return Response({}, status = status.HTTP_400_BAD_REQUEST)

        serializer = SongSerializer(song, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)