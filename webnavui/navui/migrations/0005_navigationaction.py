# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 16:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('navui', '0004_auto_20160416_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavigationAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navui.Location')),
            ],
        ),
    ]
