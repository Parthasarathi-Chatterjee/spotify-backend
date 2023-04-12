from django.db import models
from django.utils import timezone
from accounts.models import User

class Artist(models.Model):
    name = models.CharField(max_length=50, default=None, blank=True, null=True)
    image = models.ImageField(upload_to='images/artists/')
    bio = models.CharField(max_length=150, default=None, blank=True, null=True)
    dob = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
