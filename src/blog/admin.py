# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'is_draft')


# Register your models here.
admin.site.register(Post, PostAdmin)
