# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 11:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proman', '0007_auto_20161129_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='contractor',
            field=models.ForeignKey(db_column='member', on_delete=django.db.models.deletion.CASCADE, to='proman.Team', verbose_name='wykonawca'),
        ),
    ]
