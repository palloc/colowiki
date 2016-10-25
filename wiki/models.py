# coding:utf-8
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.category_name


class Article(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=1024)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.title

    
class Imagefile(models.Model):
    article = models.ForeignKey(Article)
    imagedata = models.ImageField(upload_to='images')
    date = models.DateTimeField(default=datetime.now)
    
