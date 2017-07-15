# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import markdown2 as markdown

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.safestring import mark_safe


class PostManager(models.Manager):
    def active(self):
        return super(PostManager, self).filter(is_draft=False)


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_draft = models.BooleanField(default=True)

    objects = PostManager()

    def __str__(self):
        return self.title

    def content_as_html(self):
        """ Converts markdown syntax in content field to HTML"""
        return mark_safe(markdown.markdown(self.content, extras=["fenced-code-blocks"]))
