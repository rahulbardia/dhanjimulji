# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 15:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20171105_0952'),
        ('indents', '0004_auto_20171101_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='tenant',
        ),
        migrations.RemoveField(
            model_name='buyerbanking',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='salesman',
            name='tenant',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='tenant',
        ),
        migrations.RemoveField(
            model_name='supplierbanking',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='supplierchild',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='supplierchild',
            name='tenant',
        ),
        migrations.RemoveField(
            model_name='supplierchildbanking',
            name='supplier_child',
        ),
        migrations.RemoveField(
            model_name='supplierinventory',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='supplierinventory',
            name='supplier_child',
        ),
        migrations.RemoveField(
            model_name='supplierinventory',
            name='tenant',
        ),
        migrations.AddField(
            model_name='confirmationorder',
            name='sub_tenant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.SubTenant'),
        ),
        migrations.AddField(
            model_name='indentorder',
            name='sub_tenant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.SubTenant'),
        ),
        migrations.AddField(
            model_name='indents',
            name='buyer_child',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.BuyerChild'),
        ),
        migrations.AddField(
            model_name='indents',
            name='sub_tenant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.SubTenant'),
        ),
        migrations.AlterField(
            model_name='confirmationorder',
            name='remarks',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='indentorder',
            name='remarks',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='indentorder',
            name='supplier_inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.SupplierInventory'),
        ),
        migrations.AlterField(
            model_name='indents',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Buyer'),
        ),
        migrations.AlterField(
            model_name='indents',
            name='remarks',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='indents',
            name='salesman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Salesman'),
        ),
        migrations.AlterField(
            model_name='indents',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Supplier'),
        ),
        migrations.AlterField(
            model_name='indents',
            name='supplier_child',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.SupplierChild'),
        ),
        migrations.AlterField(
            model_name='transport',
            name='office_no',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.DeleteModel(
            name='Buyer',
        ),
        migrations.DeleteModel(
            name='BuyerBanking',
        ),
        migrations.DeleteModel(
            name='Salesman',
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
        migrations.DeleteModel(
            name='SupplierBanking',
        ),
        migrations.DeleteModel(
            name='SupplierChild',
        ),
        migrations.DeleteModel(
            name='SupplierChildBanking',
        ),
        migrations.DeleteModel(
            name='SupplierInventory',
        ),
    ]
