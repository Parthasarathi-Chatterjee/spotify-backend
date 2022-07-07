from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('add/song', views.addSong, name="add-song"),
    path('upload/song', views.uploadSong, name="upload-song"),

    path('add/artist', views.addArtist, name="add-artist"),
    path('upload/artist', views.uploadArtist, name="upload-artist"),

]