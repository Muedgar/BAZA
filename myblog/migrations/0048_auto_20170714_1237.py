# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0047_auto_20170714_1119'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Player_Profile',
        ),
        migrations.DeleteModel(
            name='YouModel',
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(null=True, upload_to='image'),
        ),
    ]
