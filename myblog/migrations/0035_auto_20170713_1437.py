# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 12:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0034_auto_20170713_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='school',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]