# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from dmtc.users.models import BaseModel, Tenant, SubTenant, Buyer, \
    BuyerChild, Supplier, SupplierChild, SupplierInventory, Salesman, DmtcUser

# Create your models here.


class Transport(BaseModel):
    transport_name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=12)
    office_no = models.CharField(max_length=12, null=True)
    email = models.EmailField()


class Indents(BaseModel):
    tenant = models.ForeignKey(Tenant)
    sub_tenant = models.ForeignKey(SubTenant, null=True)
    indent_no = models.CharField(primary_key=True, max_length=255)
    indent_date = models.DateTimeField(default=timezone.now)
    buyer = models.ForeignKey(Buyer)
    buyer_child = models.ForeignKey(BuyerChild, null=True)
    supplier = models.ForeignKey(Supplier)
    supplier_child = models.ForeignKey(SupplierChild, null=True)
    bank_name = models.CharField(max_length=255)
    cash_discount = models.FloatField()
    scheme = models.CharField(max_length=255)
    payment_day = models.IntegerField()
    credit_day = models.IntegerField()
    interest_rate = models.FloatField()
    pending = models.BooleanField(default=True)
    salesman = models.ForeignKey(Salesman)
    transport = models.ForeignKey(Transport)
    indent_from = models.CharField(max_length=255)
    indent_to = models.CharField(max_length=255)
    export_to = models.CharField(max_length=255)
    prepared_by = models.ForeignKey(DmtcUser, null=True)
    remarks = models.CharField(max_length=1000, null=True)


class IndentOrder(BaseModel):
    tenant = models.ForeignKey(Tenant)
    sub_tenant = models.ForeignKey(SubTenant, null=True)
    indent = models.ForeignKey(Indents)
    supplier_inventory = models.ForeignKey(SupplierInventory)
    bales = models.IntegerField()
    remarks = models.CharField(max_length=1000, null=True)


class ConfirmationOrder(BaseModel):
    tenant = models.ForeignKey(Tenant)
    sub_tenant = models.ForeignKey(SubTenant, null=True)
    indent = models.ForeignKey(Indents)
    indent_order = models.ForeignKey(IndentOrder, null=True)
    packing = models.IntegerField()
    description = models.CharField(max_length=1000, null=True)
    quality = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)
    sort_no = models.CharField(max_length=255)
    bales = models.IntegerField()
    size = models.IntegerField()
    rate = models.FloatField()
    prepared_by = models.ForeignKey(DmtcUser, null=True)
    remarks = models.CharField(max_length=1000, null=True)
