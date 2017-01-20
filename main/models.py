from __future__ import unicode_literals
from django.db import models
from django.shortcuts import render
from django.contrib.auth.models import User

class Sucursales_Usuarios(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
