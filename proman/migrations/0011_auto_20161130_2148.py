# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 20:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proman', '0010_auto_20161130_2144'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='team',
            unique_together=set([]),
        ),
    ]
