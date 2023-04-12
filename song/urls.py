from django.urls import path
from django.contrib import admin
# from . import views
from .views import SongView

urlpatterns = [
    # path('', views.index, name="index"),

    # path('add/song', views.addSong, name="add-song"),
    # path('upload/song', views.uploadSong, name="upload-song"),
    
    path('', SongView.as_view(), name="song-list"),
]