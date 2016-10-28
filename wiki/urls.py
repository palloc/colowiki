from django.conf.urls import url, include
from django.contrib.auth.views import *
from django.views.generic.base import *
from wiki import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/(?P<category_id>\d+)/$', views.article_list, name='list'),
    url(r'^article/(?P<article_id>\d+)/$', views.article, name='article'),
    url(r'^article/(?P<article_id>\d+)$/edit/', views.article_edit, name='article_edit'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
]
