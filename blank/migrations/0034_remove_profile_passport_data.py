# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 04:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blank', '0033_auto_20171125_0423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='passport_data',
        ),
    ]