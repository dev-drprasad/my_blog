# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 14:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20170727_1338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='is_draft',
            new_name='publish',
        ),
    ]
