# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 15:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indents', '0002_auto_20171101_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indents',
            name='indent_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 1, 20, 52, 58, 252797)),
        ),
    ]
