# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-18 10:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20171018_0931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='Difficulty',
            new_name='difficulty',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='Topic',
            new_name='topic',
        ),
    ]
