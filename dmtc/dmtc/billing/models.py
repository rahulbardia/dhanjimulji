# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from dmtc.indents.models import Indents, Transport
from dmtc.users.models import BaseModel, Tenant, SubTenant, DmtcUser
from dmtc.indents.models import IndentOrder

# Create your models here.


class Bill(BaseModel):
    tenant = models.ForeignKey(Tenant)
    sub_tenant = models.ForeignKey(SubTenant, null=True)
    indent = models.ForeignKey(Indents)
    buyer_name = models.CharField(max_length=255)
    supplier_name = models.CharField(max_length=255)
    prepared_by = models.ForeignKey(DmtcUser, null=True)


class BillOrder(BaseModel):
    tenant = models.ForeignKey(Tenant)
    sub_tenant = models.ForeignKey(SubTenant, null=True)
    bill_date = models.DateTimeField(default=timezone.now)
    bill = models.ForeignKey(Bill)
    indent_order = models.ForeignKey(IndentOrder, null=True)
    quality = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)
    sort_no = models.CharField(max_length=255)
    bales = models.IntegerField()
    cuts = models.IntegerField()
    size = models.IntegerField()
    rate = models.FloatField()
    dispatch_no = models.CharField(max_length=255)
    dispatch_date = models.DateTimeField()
    transport = models.ForeignKey(Transport)
    lorry_no = models.CharField(max_length=255)
    lorry_date = models.DateTimeField()
    lorry_fare = models.FloatField()
    lorry_from = models.CharField(max_length=255)
    lorry_to = models.CharField(max_length=255)
    courier_no = models.CharField(max_length=255)
    courier_date = models.DateTimeField(null=True)
    bill_sent = models.BooleanField(default=False)
    bill_sent_date = models.BooleanField(default=False)
    remarks = models.CharField(null=True, default='', max_length=500)


class Discrepancy(BaseModel):
    tenant = models.ForeignKey(Tenant)
    sub_tenant = models.ForeignKey(SubTenant, null=True)
    bill_no = models.ForeignKey(Bill)
    bill_order = models.ForeignKey(BillOrder, null=True)
    quality = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)
    is_short = models.BooleanField()
    sort_no = models.CharField(max_length=255)
    bales = models.IntegerField()
    size = models.IntegerField()
    rate = models.IntegerField()
    prepared_by = models.ForeignKey(DmtcUser, null=True)
    remarks = models.CharField(null=True, default='', max_length=500)
