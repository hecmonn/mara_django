# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='av',
            name='money_card',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
            preserve_default=False,
        ),
    ]