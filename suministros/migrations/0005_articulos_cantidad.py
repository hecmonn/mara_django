# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 23:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suministros', '0004_auto_20170114_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulos',
            name='cantidad',
            field=models.PositiveSmallIntegerField(default=0, verbose_name=0),
            preserve_default=False,
        ),
    ]