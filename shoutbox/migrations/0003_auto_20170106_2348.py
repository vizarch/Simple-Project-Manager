# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-06 22:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shoutbox', '0002_auto_20170106_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data utworzenia'),
        ),
    ]
