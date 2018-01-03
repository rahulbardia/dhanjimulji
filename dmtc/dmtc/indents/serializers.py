from models import Transport, Indents, IndentOrder, ConfirmationOrder

from dmtc.users.serializers import BaseSerializer


class DmtcTransportSerializer(BaseSerializer):
    class Meta:
        model = Transport
        fields = ('transport_name', 'mobile_no', 'office_no', 'email')


class DmtcIndentSerializer(BaseSerializer):
    class Meta:
        model = Indents
        fields = '__all__'


class DmtcIndentOrderSerializer(BaseSerializer):
    class Meta:
        model = IndentOrder
        fields = '__all__'

# Serializer for IndentOrder per data
# class DmtcIndentOrderSerializer(serializers.Serializer):
#     tenant = serializers.IntegerField()
#     sub_tenant = serializers.IntegerField()
#     indent = serializers.IntegerField()
#     supplier = serializers.CharField()
#     supplier_child = serializers.CharField(required=False)
#     quality = serializers.CharField()
#     item_name = serializers.CharField()
#     sort_no = serializers.CharField()
#     packing = serializers.IntegerField()
#     size = serializers.IntegerField()
#     rate = serializers.IntegerField()
#     cuts = serializers.IntegerField()
#     inventory_description = serializers.CharField()
#     bales = serializers.IntegerField()
#     remarks = serializers.CharField(required=False)


class DmtcConfirmationOrderSerializer(BaseSerializer):
    class Meta:
        model = ConfirmationOrder
        fields = '__all__'