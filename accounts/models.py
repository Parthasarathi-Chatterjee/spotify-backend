from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):
    """ This class is Base User Manager """
    def create_user(self, email, password, **kwargs):
        if not email: 
            raise ValueError(_("Email should not be None"))
        if not password: 
            raise ValueError(_("Password should not be None"))

        user = self.model(email = self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        if not password:
            raise ValueError(_("Password should not be None"))

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()
        return user

class User(AbstractUser):
    # These fields tie to the roles!
    ADMIN = 1
    USER = 2

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (USER, 'User')
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    username = None
    email = models.EmailField(unique=True, primary_key=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)

    date_of_joining = models.DateTimeField(default=timezone.now) # auto_now_add=True, 
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
