# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.mail import send_mail
from django.http.response import JsonResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from blog.models import Post

NO_SENT_EMAILS = 0


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    queryset = Post.objects.active()
    extra_context = {'blog_title': settings.BLOG_TITLE}

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

class PostDetail(DetailView):
    model = Post
    queryset = Post.objects.active()


def contact(request):
    global NO_SENT_EMAILS
    if NO_SENT_EMAILS >= 50:
        return JsonResponse({'success': False})

    name = request.GET.get('name')
    email = request.GET.get('email')
    message = request.GET.get('message')

    if name and email and message:
        response = send_mail(
            'Message from contact form',
            'Name: {0} \nEmail: {1} \nMessage: {2}'.format(name, email, message),
            settings.FROM_EMAIL,
            [settings.TO_EMAIL],
        )

        NO_SENT_EMAILS += 1
        if response == 1:
            return JsonResponse({'success': True})

    return JsonResponse({'success': False})
