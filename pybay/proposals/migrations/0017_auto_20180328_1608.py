# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-03-28 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0016_auto_20180326_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talkproposal',
            name='category',
            field=models.CharField(choices=[('python fundamentals & popular libraries', 'Python Fundamentals & Popular Libraries'), ('machine learning, ai, & all things data', 'Machine Learning, AI, & All things Data'), ('devops, automation, & testing', 'DevOps, Automation, & Testing'), ('dealing with speed, scale, & performance', 'Dealing with Speed, Scale, & Performance'), ('engineering a community', 'Engineering a Community'), ('hacking hardware', 'Hacking Hardware')], max_length=250),
        ),
        migrations.AlterField(
            model_name='tutorialproposal',
            name='category',
            field=models.CharField(choices=[('python fundamentals & popular libraries', 'Python Fundamentals & Popular Libraries'), ('machine learning, ai, & all things data', 'Machine Learning, AI, & All things Data'), ('devops, automation, & testing', 'DevOps, Automation, & Testing'), ('dealing with speed, scale, & performance', 'Dealing with Speed, Scale, & Performance'), ('engineering a community', 'Engineering a Community'), ('hacking hardware', 'Hacking Hardware')], max_length=250),
        ),
    ]
