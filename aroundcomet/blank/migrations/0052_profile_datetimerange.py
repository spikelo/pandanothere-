# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blank', '0051_auto_20171204_0533'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='datetimerange',
            field=models.DateField(blank=True, help_text='Для фильтрации дат с отметками , ОТ -- К ', null=True),
        ),
    ]