from django.urls import path
from django.contrib import admin
from .views import ArtistView

urlpatterns = [
    # path('', views.index, name="index"),

    # path('add/artist', views.addArtist, name="add-artist"),
    # path('upload/artist', views.uploadArtist, name="upload-artist"),

    path('', ArtistView.as_view(), name="song-list")
]