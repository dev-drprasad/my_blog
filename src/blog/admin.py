# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm

from blog.forms import PostForm, AuthorForm
from blog.models import Post, Author, Tag


class PostAdmin(admin.ModelAdmin):
    form = PostForm

    list_display = ('title', 'created_on', 'publish')

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

    class Media:
        css = {
            'all': ('blog-default.css',)
        }


class AuthorAdmin(admin.ModelAdmin):
    form = AuthorForm
    add_form = UserCreationForm

    fieldsets = (
        (None, {'fields': (
            ('first_name', 'last_name',),
            ('email', 'website'),
            'password',
            'is_active',
            'avatar',
            'about',
        )}),
    )


class TagAdmin(admin.ModelAdmin):
    pass


admin.site.site_header = 'My Blog'
admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
