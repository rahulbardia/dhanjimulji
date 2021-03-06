# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-17 06:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20171117_0021'),
        ('indents', '0005_auto_20171105_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmationorder',
            name='indent_order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='indents.IndentOrder'),
        ),
        migrations.AddField(
            model_name='confirmationorder',
            name='prepared_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.DmtcUser'),
        ),
        migrations.AddField(
            model_name='indents',
            name='prepared_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.DmtcUser'),
        ),
        migrations.AlterField(
            model_name='confirmationorder',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='indents',
            name='pending',
            field=models.BooleanField(default=True),
        ),
    ]
