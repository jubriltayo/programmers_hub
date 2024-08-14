from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .manager import UserManager



class User(AbstractBaseUser):
    userId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50, null=False)
    lastName = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, unique=True, null=False)
    phone = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to='avatars', blank=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName', 'lastName']

    def __str__(self):
        return self.email