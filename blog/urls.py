from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
    url(r'^logged_out$', views.logged_out, name='logged_out'),
    url(r'^delete/post/(?P<post_id>\d+)/comment/(?P<comment_id>\d+)/$', views.comment_delete, name='comment_delete'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^category/(?P<category_text>.*)/$', views.get_category, name='get_category'),
    url(r'^profile/edit/$', views.update_profile, name='update_profile'),
    url(r'^profile/$', views.show_profile, name='show_profile'),
    url(r'^profile/(?P<pk>\d+)/$', views.user_profile, name='user_profile'),
    url(r'^post/(?P<pk>\d+)/like/$', views.like, name='like'),
    url(r'^post/(?P<pk>\d+)/unlike/$', views.like, name='unlike'),
    url(r'^most_popular/$', views.most_popular, name='most_popular'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
