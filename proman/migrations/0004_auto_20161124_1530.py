# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 14:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proman', '0003_auto_20161123_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Treść')),
            ],
            options={
                'verbose_name_plural': 'notatki',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('startdate', models.DateTimeField(auto_now_add=True, verbose_name='Data rozpoczęcia')),
                ('enddate', models.DateTimeField(verbose_name='Data zakończenia')),
                ('path', models.FilePathField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'projekty',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'zadania',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'zespoły',
            },
        ),
        migrations.RemoveField(
            model_name='notatka',
            name='zadanie',
        ),
        migrations.RemoveField(
            model_name='projekt',
            name='wlasciciel',
        ),
        migrations.RemoveField(
            model_name='zadanie',
            name='projekt',
        ),
        migrations.RemoveField(
            model_name='zadanie',
            name='wykonawca',
        ),
        migrations.AlterUniqueTogether(
            name='zespol',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='zespol',
            name='czlonek',
        ),
        migrations.RemoveField(
            model_name='zespol',
            name='projekt',
        ),
        migrations.AlterModelOptions(
            name='uzytkownik',
            options={'verbose_name_plural': 'użytkownicy'},
        ),
        migrations.DeleteModel(
            name='Notatka',
        ),
        migrations.DeleteModel(
            name='Projekt',
        ),
        migrations.DeleteModel(
            name='Zadanie',
        ),
        migrations.DeleteModel(
            name='Zespol',
        ),
        migrations.AddField(
            model_name='team',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proman.Uzytkownik'),
        ),
        migrations.AddField(
            model_name='team',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proman.Project'),
        ),
        migrations.AddField(
            model_name='task',
            name='contractor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proman.Team'),
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proman.Project'),
        ),
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proman.Uzytkownik', verbose_name='Właściciel'),
        ),
        migrations.AddField(
            model_name='note',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proman.Task'),
        ),
        migrations.AlterUniqueTogether(
            name='team',
            unique_together=set([('project', 'member')]),
        ),
    ]
