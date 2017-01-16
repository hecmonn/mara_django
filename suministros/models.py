from __future__ import unicode_literals
from rh.models import Sucursales as sid
from django.db import models

class Articulos(models.Model):
    articulo=models.CharField(max_length=50)
    TYPE_CHOICES=(
        ('oficina','Oficina'),
        ('limpieza','Limpieza'),
    )
    created_date=models.DateField(auto_now=True)
    tipo=models.CharField(max_length=50,choices=TYPE_CHOICES)
    def __str__(self):
        return self.articulo

class Pedidos(models.Model):
    suc=models.ForeignKey(sid)
    articulo=models.ForeignKey(Articulos)
    cantidad=models.PositiveSmallIntegerField(0)
    created_date=models.DateTimeField(auto_now=True)
