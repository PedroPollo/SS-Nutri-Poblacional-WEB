from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    nombre = models.TextField(max_length=100)
    curp = models.TextField(max_length=19)