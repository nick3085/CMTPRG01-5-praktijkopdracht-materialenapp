# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-28 14:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('materialmanager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='test',
        ),
        migrations.AddField(
            model_name='delivery',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='materialmanager.Supplier'),
        ),
    ]