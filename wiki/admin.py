from django.contrib import admin
from wiki.models import *

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Imagefile)

# Register your models here.
