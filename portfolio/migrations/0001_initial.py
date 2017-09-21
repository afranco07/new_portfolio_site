# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 19:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('img_source', models.URLField()),
                ('info', models.TextField()),
                ('gif', models.URLField()),
                ('github', models.URLField()),
                ('website', models.URLField()),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Language')),
            ],
        ),
    ]
