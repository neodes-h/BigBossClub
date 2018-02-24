# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-02-20 00:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bbc_db', '0013_auto_20180220_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='id',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='att_date',
            field=models.DateField(db_column='ATT_DATE', primary_key=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='class_field',
            field=models.ForeignKey(db_column='CLASS_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='bbc_db.Class'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='std',
            field=models.ForeignKey(db_column='STD_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, to='bbc_db.Student'),
        ),
    ]