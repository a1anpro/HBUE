# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-14 04:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hbue', '0008_auto_20171104_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commentTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 14, 4, 48, 49, 127897, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='ifPass',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=33),
        ),
    ]