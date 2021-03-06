# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('description', models.CharField(max_length=255)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('beds', models.IntegerField()),
                ('baths', models.IntegerField()),
                ('square_meters', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('x_u', models.IntegerField()),
                ('y_u', models.IntegerField()),
                ('x_b', models.IntegerField()),
                ('y_b', models.IntegerField()),
            ],
        ),
    ]
