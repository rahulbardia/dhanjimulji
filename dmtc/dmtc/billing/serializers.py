from models import Bill, BillOrder

from dmtc.users.serializers import BaseSerializer


class DmtcBillSerializer(BaseSerializer):
    class Meta:
        model = Bill
        fields = '__all__'


class DmtcBillOrderSerializer(BaseSerializer):
    class Meta:
        model = BillOrder
        fields = '__all__'

