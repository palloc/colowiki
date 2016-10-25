# coding:utf-8
from django.shortcuts import render, get_object_or_404, Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader, Context
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import logout, views
from django.contrib.auth.models import User
from models import *

# Top page's view
def index(request):
    return render(request, 'wiki/index.html')

# Article's view
def article(request, article_id):
    return render(request, 'wiki/article.html', {'id': article_id})

# Article's edit view
def article_edit(request, article_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/article/' + article_id + '/')
    return render(request, 'wiki/article_edit.html', {'id': article_id})

# Logout view
def logout_view(request):
    logout(request)
    return render(request)

# 
    


