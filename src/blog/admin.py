# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from blog.forms import PostForm
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    form = PostForm

    list_display = ('title', 'created_on', 'is_draft')


admin.site.site_header = 'My Blog'
admin.site.register(Post, PostAdmin)
