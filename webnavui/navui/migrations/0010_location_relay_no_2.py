# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navui', '0009_auto_20160416_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='relay_no_2',
            field=models.IntegerField(default=0),
        ),
    ]