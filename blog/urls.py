from django.conf.urls import url
from blog import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^post/new/', views.CreatePostView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/$', views.DetailPostView.as_view(), name='post_detail'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.EditPostView.as_view(), name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.DeletePostView.as_view(), name='post_delete'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.publish_post, name='post_publish'),
    url(r'^drafts/$', views.DraftsListView.as_view(), name='drafts'),
    url(r'^works/$', views.AllWorksListView.as_view(), name='works'),
]
