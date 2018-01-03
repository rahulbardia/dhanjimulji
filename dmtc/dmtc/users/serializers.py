from rest_framework import serializers
from models import BaseModel, Tenant, DmtcUser,\
    Buyer, Supplier, SupplierInventory, Salesman


# class TenantSerializer(serializers.Serializer):
#     name = serializers.CharField(required=False, allow_blank=True)
#     place = serializers.CharField(required=True, allow_blank=False)
#     address = serializers.CharField(required=False, allow_blank=True)
#     mobile_no = serializers.CharField(required=True, allow_blank=False)
#     gst_no = serializers.CharField(required=False, allow_blank=True)
#     office_no = serializers.CharField(required=False, allow_blank=True)
#     company = serializers.CharField(required=False, allow_blank=True)
#     email = serializers.EmailField()
#     bank = serializers.CharField(required=False, allow_blank=True)
#     bank_account = serializers.CharField(required=False, allow_blank=True)
#     user_count = serializers.IntegerField()
#
#     def create(self, validate_data):
#         return Tenant.objects.create(**validate_data)

class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        model = BaseModel
        fields = ('id', 'created_date', 'updated_date', 'active')


class TenantSerializer(BaseSerializer):
    class Meta:
        model = Tenant
        fields = ('id', 'place', 'name', 'address', 'mobile_no', 'gst_no',
                  'office_no', 'company', 'email', 'user_count')


class DmtcUserSerializer(BaseSerializer):
    class Meta:
        model = DmtcUser
        fields = ('user', 'tenant', 'place', 'address', 'mobile_no',
                  'email', 'is_admin')


class DmtcBuyerSerializer(BaseSerializer):
    class Meta:
        model = Buyer
        fields = ('id', 'tenant', 'sub_tenant', 'name', 'place', 'address',
                  'mobile_no', 'office_no', 'email', 'gst_no', 'pan_no',
                  'credit_limit', 'total_credit')


class DmtcSupplierSerializer(BaseSerializer):
    class Meta:
        model = Supplier
        fields = ('id', 'tenant', 'sub_tenant', 'name', 'place', 'address',
                  'mobile_no', 'office_no', 'email', 'gst_no', 'pan_no',
                  'commission_percentage', 'credit_limit', 'total_credit')


class DmtcSupplierInventorySerializer(BaseSerializer):
    class Meta:
        model = SupplierInventory
        fields = ('id', 'tenant', 'sub_tenant', 'supplier', 'supplier_child',
                  'quality', 'item_name', 'sort_no', 'packing', 'size',
                  'rate', 'cuts', 'description')


class DmtcSalesmanSerializer(BaseSerializer):
    class Meta:
        model = Salesman
        fields = ('id', 'tenant', 'sub_tenant', 'name', 'phone_no', 'address',
                  'place', 'email', 'commission_percentage')
