# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models
# Create your models here.


class BaseModel(models.Model):

    created_date = models.DateTimeField(editable=False, auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def soft_delete(self):
        """
        Override delete for soft delete
        :param using:
        :return:
        """
        self.active = False
        self.save()


class Tenant(BaseModel):
    name = models.CharField(max_length=255, null=True)
    place = models.CharField(max_length=255)
    address = models.CharField(max_length=500, null=True)
    mobile_no = models.CharField(max_length=12)
    gst_no = models.CharField(max_length=15, null=True)
    office_no = models.CharField(max_length=12, null=True)
    company = models.CharField(max_length=255)
    email = models.EmailField()
    user_count = models.IntegerField()


class TenantBanking(BaseModel):
    tenant = models.ForeignKey(Tenant)
    bank = models.CharField(max_length=255, null=True)
    bank_account = models.CharField(max_length=20, null=True, unique=True)


class SubTenant(BaseModel):
    tenant = models.ForeignKey(Tenant)
    name = models.CharField(max_length=255, null=True)
    place = models.CharField(max_length=255)
    address = models.CharField(max_length=500, null=True)
    mobile_no = models.CharField(max_length=12)
    gst_no = models.CharField(max_length=15, null=True)
    office_no = models.CharField(max_length=12, null=True)
    company = models.CharField(max_length=255)
    email = models.EmailField()
    user_count = models.IntegerField()


class SubTenantBanking(BaseModel):
    sub_tenant = models.ForeignKey(SubTenant)
    bank = models.CharField(max_length=255, null=True)
    bank_account = models.CharField(max_length=20, null=True, unique=True)


class DmtcUser(BaseModel):
    tenant = models.ForeignKey(Tenant)
    sub_tenant = models.ForeignKey(SubTenant, null=True)
    user = models.OneToOneField(User)
    place = models.CharField(max_length=255)
    address = models.CharField(max_length=500, null=True)
    mobile_no = models.CharField(max_length=12, null=True)
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField()


class Buyer(BaseModel):
    tenant = models.ForeignKey(Tenant)
    sub_tenant = models.ForeignKey(SubTenant, null=True)
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    address = models.CharField(max_length=500, null=True)
    mobile_no = models.CharField(max_length=12)
    office_no = models.CharField(max_length=12, null=True)
    email = models.EmailField()
    gst_no = models.CharField(max_length=15, null=True)
    pan_no = models.CharField(max_length=10, null=True)
    credit_limit = models.IntegerField()
    total_credit = models.IntegerField(default=0)


class BuyerBanking(BaseModel):
    buyer = models.ForeignKey(Buyer)
    bank = models.CharField(max_length=255)
    bank_account = models.CharField(max_length=20, null=True, unique=True)


class BuyerChild(BaseModel):
    tenant = models.ForeignKey(Tenant)
    sub_tenant = models.ForeignKey(SubTenant, null=True)
    buyer = models.ForeignKey(Buyer)
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    address = models.CharField(max_length=500, null=True)
    email = models.EmailField(null=True)
    mobile_no = models.CharField(max_length=12, null=True)
    office_no = models.CharField(max_length=12, null=True)
    gst_no = models.CharField(max_length=15, null=True)
    pan_no = models.CharField(max_length=10, null=True)
    commission_percentage = models.FloatField(default=0)


class BuyerChildBanking(BaseModel):
    buyer_child = models.ForeignKey(BuyerChild)
    bank = models.CharField(max_length=255)
    bank_account = models.CharField(max_length=20, null=True, unique=True)


class Supplier(BaseModel):
    tenant = models.ForeignKey(Tenant)
    sub_tenant = models.ForeignKey(SubTenant, null=True)
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    address = models.CharField(max_length=500, null=True)
    mobile_no = models.CharField(max_length=12)
    office_no = models.CharField(max_length=12, null=True)
    email = models.EmailField()
    gst_no = models.CharField(max_length=15, null=True)
    pan_no = models.CharField(max_length=10, null=True)
    commission_percentage = models.FloatField()
    credit_limit = models.IntegerField(default=0, null=True)
    total_credit = models.IntegerField(default=0, null=True)


class SupplierBanking(BaseModel):
    supplier = models.ForeignKey(Supplier)
    bank = models.CharField(max_length=255)
    bank_account = models.CharField(max_length=20, null=True, unique=True)


class SupplierChild(BaseModel):
    tenant = models.ForeignKey(Tenant)
    sub_tenant = models.ForeignKey(SubTenant, null=True)
    supplier = models.ForeignKey(Supplier)
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    address = models.CharField(max_length=500, null=True)
    mobile_no = models.CharField(max_length=12)
    office_no = models.CharField(max_length=12, null=True)
    email = models.EmailField()
    gst_no = models.CharField(max_length=15, null=True)
    pan_no = models.CharField(max_length=10, null=True)
    commission_percentage = models.FloatField()


class SupplierChildBanking(BaseModel):
    supplier_child = models.ForeignKey(SupplierChild)
    bank = models.CharField(max_length=255)
    bank_account = models.CharField(max_length=20, null=True, unique=True)


class SupplierInventory(BaseModel):
    tenant = models.ForeignKey(Tenant)
    sub_tenant = models.ForeignKey(SubTenant, null=True)
    supplier = models.ForeignKey(Supplier)
    supplier_child = models.ForeignKey(SupplierChild, null=True)
    quality = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)
    sort_no = models.CharField(max_length=255)
    packing = models.IntegerField()
    size = models.IntegerField()
    rate = models.FloatField()
    cuts = models.IntegerField()
    description = models.CharField(max_length=1000, null=True)


class Salesman(BaseModel):
    tenant = models.ForeignKey(Tenant)
    sub_tenant = models.ForeignKey(SubTenant, null=True)
    name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=12)
    address = models.CharField(max_length=500, null=True)
    place = models.CharField(max_length=255)
    email = models.EmailField()
    commission_percentage = models.FloatField(default=0, null=True)

