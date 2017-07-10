from django.conf.urls import url

from blog.views import PostList, PostDetail

urlpatterns = [
    url(r'^posts/', PostList.as_view(), name='posts-list'),
    url(r'^post/(?P<pk>\d+)/$', PostDetail.as_view(), name='post-detail'),
]