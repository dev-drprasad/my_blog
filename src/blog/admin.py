# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Post, PostAdmin)
