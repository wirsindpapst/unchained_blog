# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-27 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20161127_2214'),
    ]

    operations = [
    
        migrations.RemoveField(
            model_name='post',
            name='summary',
        ),
    ]
