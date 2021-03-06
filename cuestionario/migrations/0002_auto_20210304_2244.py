# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2021-03-04 21:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuestionario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50, unique=True)),
                ('nombre', models.TextField(default='')),
                ('descripcion', models.TextField(default='')),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.AddField(
            model_name='pregunta',
            name='Encuesta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pregunta', to='cuestionario.Encuesta'),
            preserve_default=False,
        ),
    ]