# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from blog.models import Post


class PostList(ListView):
    model = Post
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post
