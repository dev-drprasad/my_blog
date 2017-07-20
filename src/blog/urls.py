from django.conf.urls import url

from blog.views import PostList, PostDetail, contact

urlpatterns = [
    url(r'^$', PostList.as_view(), name='posts-list'),
    url(r'^article/(?P<slug>[-\w]+)/$', PostDetail.as_view(), name='post-detail'),
    url(r'^contact/$', contact, name='contact'),
]