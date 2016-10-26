# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 03:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Imagefile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagedata', models.ImageField(upload_to='images')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.Article')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.Category'),
        ),
    ]