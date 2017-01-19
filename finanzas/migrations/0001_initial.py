# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 01:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rh', '0003_auto_20170117_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Av',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket1', models.PositiveIntegerField(default=0)),
                ('ticket2', models.PositiveIntegerField(default=0)),
                ('bmx', models.DecimalField(decimal_places=2, max_digits=20)),
                ('bbjio', models.DecimalField(decimal_places=2, max_digits=20)),
                ('amex', models.DecimalField(decimal_places=2, max_digits=20)),
                ('scotia_bank', models.DecimalField(decimal_places=2, max_digits=20)),
                ('santander', models.DecimalField(decimal_places=2, max_digits=20)),
                ('vales_caja', models.DecimalField(decimal_places=2, max_digits=20)),
                ('univale', models.DecimalField(decimal_places=2, max_digits=20)),
                ('coppel', models.DecimalField(decimal_places=2, max_digits=20)),
                ('coupon_cloud', models.DecimalField(decimal_places=2, max_digits=20)),
                ('efectivo', models.DecimalField(decimal_places=2, max_digits=20)),
                ('dolares', models.DecimalField(decimal_places=2, max_digits=20)),
                ('tot_tarjetas', models.DecimalField(decimal_places=2, max_digits=20)),
                ('fondo', models.DecimalField(decimal_places=2, max_digits=20)),
                ('tot_dia', models.DecimalField(decimal_places=2, max_digits=20)),
                ('corte_caja', models.DecimalField(decimal_places=2, max_digits=20)),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rh.Sucursales')),
            ],
        ),
    ]
