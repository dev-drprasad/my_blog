# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_is_draft'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='some-slug'),
            preserve_default=False,
        ),
    ]
