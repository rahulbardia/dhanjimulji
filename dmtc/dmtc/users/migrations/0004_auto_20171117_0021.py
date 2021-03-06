# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-17 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20171105_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyerbanking',
            name='bank_account',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='buyerchildbanking',
            name='bank_account',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='salesman',
            name='commission_percentage',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='subtenantbanking',
            name='bank_account',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='credit_limit',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='total_credit',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='supplierbanking',
            name='bank_account',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='supplierchildbanking',
            name='bank_account',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='supplierinventory',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='tenantbanking',
            name='bank_account',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
