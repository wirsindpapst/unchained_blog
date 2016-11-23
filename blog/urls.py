from django.conf.urls import url
from . import views

# Additional imports for users:
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^accounts/register/$',views.register, name='register'),
    url(r'^emoji/', include('emoji.urls')),
    url(r'^delete/post/(?P<post_id>\d+)/comment/(?P<comment_id>\d+)/$', views.comment_delete, name='comment_delete'),
]
