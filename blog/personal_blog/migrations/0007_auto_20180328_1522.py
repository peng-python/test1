# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-28 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_blog', '0006_recommendmodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentencemodel',
            name='content',
            field=models.TextField(default='', max_length=200, verbose_name='\u6bcf\u65e5\u4e00\u53e5'),
        ),
    ]
