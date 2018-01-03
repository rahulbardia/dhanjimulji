# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from dmtc.billing.models import *
from dmtc.indents.models import BaseModel, Tenant, SubTenant
from dmtc.users.models import SupplierBanking, SupplierChildBanking, DmtcUser

# Create your models here.


class DraftSlip(BaseModel):
    tenant = models.ForeignKey(Tenant)
    sub_tenant = models.ForeignKey(SubTenant, null=True)
    bill = models.ForeignKey(Bill)
    bank = models.CharField(max_length=255)
    supplier_banking = models.ForeignKey(SupplierBanking, null=True)
    supplier_child_banking = models.ForeignKey(SupplierChildBanking, null=True)
    dd_no = models.CharField(max_length=6)
    cheque_no = models.CharField(max_length=6)
    amount = models.FloatField()
    cash_payment = models.BooleanField(default=False)
    prepared_by = models.ForeignKey(DmtcUser, null=True)
    description = models.CharField(max_length=1000)
    remarks = models.CharField(max_length=1000)


class CnoteDnote(BaseModel):
    tenant = models.ForeignKey(Tenant)
    sub_tenant = models.ForeignKey(SubTenant, null=True)
    bill = models.ForeignKey(Bill)
    note_no = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    dd_no = models.CharField(max_length=6)
    cheque_no = models.CharField(max_length=6)
    prepared_by = models.ForeignKey(DmtcUser, null=True)
    amount = models.FloatField()
    description = models.CharField(max_length=1000)
    remarks = models.CharField(max_length=1000)