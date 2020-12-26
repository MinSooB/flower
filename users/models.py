from django.contrib.auth.models import AbstractUser
from . import managers

class User(AbstractUser):
    objects = managers.CustomUserManager()