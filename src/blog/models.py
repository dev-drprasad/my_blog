# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import markdown2 as markdown

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.safestring import mark_safe

def upload_path_handler(instance, filename):
    import os.path
    fn, ext = os.path.splitext(filename)
    return 'post_{post_id}/cover.{ext}'.format(post_id=instance.id, ext=ext)

class PostManager(models.Manager):
    def active(self):
        return super(PostManager, self).filter(is_draft=False)


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    cover_image = models.ImageField(upload_to=upload_path_handler, blank=True, null=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_draft = models.BooleanField(default=True)

    objects = PostManager()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def content_as_html(self):
        """ Converts markdown syntax in content field to HTML"""
        return mark_safe(markdown.markdown(self.content, extras=["fenced-code-blocks"]))

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse('blog:post-detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_image = self.cover_image
            self.cover_image = None
            super(Post, self).save(*args, **kwargs)
            self.cover_image = saved_image

            # to avoid integrity error when force_insert=True
            kwargs['force_insert'] = False

        super(Post, self).save(*args, **kwargs)
