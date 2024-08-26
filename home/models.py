from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    nickname = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 254, verbose_name = 'email address', unique = True)
    pass
