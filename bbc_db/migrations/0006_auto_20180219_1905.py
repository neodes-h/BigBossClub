# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-02-19 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbc_db', '0005_auto_20180217_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='class_time',
            field=models.CharField(blank=True, db_column='CLASS_TIME', max_length=45, null=True),
        ),
    ]