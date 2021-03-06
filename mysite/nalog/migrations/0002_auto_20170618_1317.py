# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userresults',
            name='checkChild',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userresults',
            name='checkInv',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userresults',
            name='countChild',
            field=models.BigIntegerField(default=2),
        ),
        migrations.AddField(
            model_name='userresults',
            name='per13',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userresults',
            name='per13div',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userresults',
            name='per30',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userresults',
            name='result',
            field=models.CharField(max_length=50),
        ),
    ]
