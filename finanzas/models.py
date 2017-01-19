from __future__ import unicode_literals
from django.db import models
from rh.models import Sucursales as Sucursal

class Av(models.Model):
    ticket1=models.PositiveIntegerField(default=0)
    ticket2=models.PositiveIntegerField(default=0)
    bmx=models.DecimalField(max_digits=20,decimal_places=2)
    bbjio=models.DecimalField(max_digits=20,decimal_places=2)
    amex=models.DecimalField(max_digits=20,decimal_places=2)
    scotia_bank=models.DecimalField(max_digits=20,decimal_places=2)
    santander=models.DecimalField(max_digits=20,decimal_places=2)
    money_card=models.DecimalField(max_digits=20,decimal_places=2)
    vales_caja=models.DecimalField(max_digits=20,decimal_places=2)
    univale=models.DecimalField(max_digits=20,decimal_places=2)
    coppel=models.DecimalField(max_digits=20,decimal_places=2)
    coupon_cloud=models.DecimalField(max_digits=20,decimal_places=2)
    efectivo=models.DecimalField(max_digits=20,decimal_places=2)
    dolares=models.DecimalField(max_digits=20,decimal_places=2)
    tot_tarjetas=models.DecimalField(max_digits=20,decimal_places=2)
    fondo=models.DecimalField(max_digits=20,decimal_places=2)
    tot_dia=models.DecimalField(max_digits=20,decimal_places=2)
    corte_caja=models.DecimalField(max_digits=20,decimal_places=2)
    sucursal=models.ForeignKey(Sucursal)

class Gastos(models.Model):
    descripcion=models.CharField(max_length=100)
    monto=models.DecimalField(max_digits=10,decimal_places=2)
    av=models.ForeignKey(Av)
