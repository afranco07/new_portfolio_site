# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-20 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='modal_title',
            field=models.CharField(default='defaultTitle', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
