# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 12:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0032_auto_20170713_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='website',
        ),
    ]