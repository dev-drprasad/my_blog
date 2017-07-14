# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import markdown

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.safestring import mark_safe


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    def content_as_html(self):
        """ Converts markdown syntax in content field to HTML"""
        return mark_safe(markdown.markdown(self.content))
