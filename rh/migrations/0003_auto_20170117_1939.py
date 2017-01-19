# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0002_empleados'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='estado',
            field=models.BooleanField(choices=[(0, 'Inactivo'), (1, 'Activo')], default=1),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='sexo',
            field=models.BooleanField(choices=[(0, 'Mujer'), (1, 'Hombre')], default=0),
        ),
    ]
