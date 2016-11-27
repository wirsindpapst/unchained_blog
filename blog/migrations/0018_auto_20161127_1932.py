# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-27 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_user'),
    ]

    migrations.AddField(
        model_name='post',
        name='likes',
        field=models.ManyToManyField(related_name='liked_posts', to='blog.Like'),
    ),
