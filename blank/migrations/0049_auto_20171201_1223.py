# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blank', '0048_auto_20171201_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, choices=[('open', 'Открыта'), ('close', 'Закрыта')], max_length=8, null=True),
        ),
    ]
