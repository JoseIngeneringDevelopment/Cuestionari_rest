# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2021-03-05 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuestionario', '0015_auto_20210305_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opcion',
            name='numero',
            field=models.CharField(default='0', max_length=32),
        ),
    ]