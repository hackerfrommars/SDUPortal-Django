# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-12 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_user', models.IntegerField(default=0)),
                ('p_pass', models.CharField(max_length=30)),
            ],
        ),
    ]
