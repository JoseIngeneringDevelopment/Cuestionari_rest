# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2021-03-05 00:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuestionario', '0005_auto_20210305_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuesta',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to='muestra.Muestra'),
        ),
    ]