# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blank', '0017_auto_20171120_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='flat',
            field=models.CharField(default='+9989', help_text='Введите номер квартиры', max_length=4),
        ),
    ]
