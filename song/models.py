from django.db import models
from django.utils import timezone
from accounts.models import User

class Artist(models.Model):
    name = models.CharField(max_length=50, default=None, blank=True, null=True)
    bio = models.CharField(max_length=150, default=None, blank=True, null=True)
    dob = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    
class Song(models.Model):
    name = models.CharField(max_length=50, default=None, blank=True, null=True)
    dateOfRelease =  models.DateTimeField(default=timezone.now)
    cover  = models.ImageField(upload_to='images/posts/')
    artist = models.ManyToManyField(Artist)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Rating(models.Model):
    user = models.ManyToManyField(User)
    song = models.ManyToManyField(Song)
    rating = models.IntegerField(default=None, blank=True, null=True)
    
    def __str__(self):
        return self.rating