from django.db import models
from django.utils import timezone
from accounts.models import User
from artist.models import Artist

class Song(models.Model):
    name = models.CharField(max_length=50, default=None, blank=True, null=True)
    dateOfRelease =  models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/songs/')
    file = models.FileField(upload_to='files/songs/')
    artist = models.ManyToManyField(Artist)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
    @property
    def coverURL(self):
        try:
            url = self.cover.url
        except:
            url = ''
        return url


class Rating(models.Model):
    user = models.ManyToManyField(User)
    song = models.ManyToManyField(Song)
    rating = models.IntegerField(default=None, blank=True, null=True)
    
    def __str__(self):
        return self.rating