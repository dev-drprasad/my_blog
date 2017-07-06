from django.conf.urls import url

from blog.views import PostList

urlpatterns = [
    url(r'^posts/', PostList.as_view(), name='posts-list'),
]