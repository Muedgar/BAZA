# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-15 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0052_auto_20170715_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='birth_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.FileField(blank=True, upload_to='documents/'),
        ),
    ]