# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 23:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apprestuser', '0005_auto_20171104_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='persona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='apprestuser.Personas'),
        ),
    ]
