# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 08:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nalog', '0002_auto_20170618_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='userresults',
            name='number',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userresults',
            name='dateStart',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 18, 8, 57, 1, 99179, tzinfo=utc)),
        ),
    ]
