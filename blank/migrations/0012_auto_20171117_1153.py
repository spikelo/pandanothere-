# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 11:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blank', '0011_auto_20171117_1146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='connectioninfo',
            old_name='Smart_tarrif',
            new_name='tarrif',
        ),
        migrations.RemoveField(
            model_name='connectioninfo',
            name='Samrt',
        ),
    ]
