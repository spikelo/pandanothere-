# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 12:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blank', '0058_auto_20171209_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='datetimerange',
            field=models.DateField(blank=True, default=django.utils.timezone.now, help_text='Для фильтрации дат с отметками , ОТ -- К', null=True),
        ),
    ]