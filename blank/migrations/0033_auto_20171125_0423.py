# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 04:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blank', '0032_auto_20171124_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tarrif',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]