from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    nombre = models.TextField(max_length=100)
    curp = models.TextField(max_length=19)
    id = models.BigAutoField(primary_key=True)

class Pollsters(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    grupo = models.CharField(max_length=10)
    unidadap = models.CharField(max_length=50)
    tuition = models.CharField(max_length=30)

class User_Pollsters(models.Model):
    STATUS = (
            ('Pendiente','Pendiente'),
            ('Aceptado','Aceptado'),
            )
    
    pollster = models.ForeignKey(Pollsters,null=False,on_delete=models.CASCADE)
    investigator = models.ForeignKey(User,null=False,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True,null=False)
    status = models.CharField(max_length=200,null=False,choices=STATUS)