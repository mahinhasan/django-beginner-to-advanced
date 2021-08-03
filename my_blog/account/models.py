from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):

    age = models.PositiveIntegerField(default=0)
