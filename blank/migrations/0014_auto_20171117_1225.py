# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blank', '0013_auto_20171117_1204'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ConnectionInfo',
        ),
        migrations.AddField(
            model_name='user',
            name='prefering_connection',
            field=models.DateField(blank=True, help_text='Предпочитаемая дата подключения', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='tarrif',
            field=models.CharField(blank=True, choices=[('s40', 'Скоростной 40'), ('s60', 'Скоростной 60'), ('s80', 'Скоростной 80'), ('s100', 'Скоростной 100'), ('s120', 'Скоростной 120'), ('s140', 'Скоростной 140'), ('s160', 'Скоростной 160'), ('s200', 'Скоростной 200'), ('s240', 'Скоростной 240')], default='s40', help_text='Предпочитаемый тарифный план', max_length=4, null=True),
        ),
    ]
