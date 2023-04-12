from django.shortcuts import redirect, render
from artist.forms import uploadArtistForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from artist.models import Artist
from artist.serializers import ArtistSerializer

# Create your views here.

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


class ArtistView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            artists = Artist.objects.all()
        except:
            return Response({}, status = status.HTTP_400_BAD_REQUEST)

        serializer = ArtistSerializer(artists, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    