# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from blog.models import Post


class PostList(ListView):
    model = Post
