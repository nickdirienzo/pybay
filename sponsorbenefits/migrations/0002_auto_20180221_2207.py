# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-02-22 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsorbenefits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benefit',
            name='price',
            field=models.IntegerField(),
        ),
    ]
