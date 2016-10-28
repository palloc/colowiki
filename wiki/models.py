# coding:utf-8
from __future__ import unicode_literals
from datetime import datetime
from django.db import models


class Bigcategory(models.Model):
    name = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    big_category = models.ForeignKey(Bigcategory)
    category_name = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.category_name


class Article(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=1024)
    text = models.TextField()
    image_data = models.ImageField(upload_to='images', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    
