# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nalog', '0006_auto_20170622_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userresults',
            name='checkChild',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userresults',
            name='checkInv',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userresults',
            name='per13',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userresults',
            name='per13div',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userresults',
            name='per30',
            field=models.CharField(max_length=50),
        ),
    ]