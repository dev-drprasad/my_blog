# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 14:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20170725_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='is_staff',
        ),
    ]