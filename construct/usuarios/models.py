from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    choices_cargo = (('V', 'Vendedor'),)
    cargo = models.CharField(max_lenth=1, choices=choices_cargo)