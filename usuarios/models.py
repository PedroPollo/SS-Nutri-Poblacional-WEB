from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=150)
    curp = models.TextField(max_length=18,unique=True)
    tuition = models.TextField(max_length=20,unique=True)
    email = models.TextField(max_length=100,unique=True)
    password = models.TextField(max_length=100)
    #Rol
    role = models.IntegerField(null=True, default=None)