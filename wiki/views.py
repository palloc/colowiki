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
    # For sidebar
    big_category = Bigcategory.objects.all()
    category = Category.objects.all()

    return render(request, 'wiki/index.html', {'category': category, 'big_cat': big_category})


# List view
def article_list(request, category_id):
    # For sidebar
    big_category = Bigcategory.objects.all()
    category = Category.objects.all()
    # Category list
    list = Article.objects.filter(id=category_id)
    
    return render(request, 'wiki/list.html', {'articles': list, 'category': category, 'big_cat': big_category})


# Article's view
def article(request, article_id):
    # For sidebar
    big_category = Bigcategory.objects.all()
    category = Category.objects.all()
    # Article data 
    article_data = get_object_or_404(Article, id=article_id)

    return render(request, 'wiki/article.html', {'article': article_data, 'category': category, 'big_cat': big_category})


# Article's edit view
def article_edit(request, article_id):
    # For sidebar
    big_category = Bigcategory.objects.all()
    category = Category.objects.all()

    # Auth
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/article/' + article_id + '/')
    article_data = get_object_or_404(Article, pk=article_id)    

    return render(request, 'wiki/article_edit.html', {'article': article_data})


# Logout view
def logout_view(request):
    logout(request)
    return render(request)

