# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blank', '0044_auto_20171201_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('open', 'Открыта'), ('new', 'Новая'), ('close', 'Закрыта')], default='open', max_length=8),
        ),
    ]
