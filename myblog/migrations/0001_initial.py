# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 08:15
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('field', models.CharField(choices=[('Physics ', 'PHY'), ('Chemistry', 'CHEM'), ('Mathematics', 'MATH'), ('Biology', 'BIO'), ('Computer', 'CS'), ('History', 'HIS'), ('Economics', 'ECON'), ('Literature', 'LIT'), ('Geography', 'GEO')], default='all', max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('check_date', models.DateField(default=datetime.date.today)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]