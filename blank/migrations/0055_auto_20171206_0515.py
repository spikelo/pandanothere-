# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blank', '0054_auto_20171206_0514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='prefering_connection',
            field=models.DateField(help_text='Предпочитаемая дата подключения'),
        ),
    ]
