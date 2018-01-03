# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.response import Response
from rest_framework import status

from dmtc.users.views import BaseApiView
from dmtc import utils
# Model Imports
from models import BillOrder,Bill

# Serializer Imports
from serializers import DmtcBillSerializer, DmtcBillOrderSerializer


# Create your views here.

class DmtcBill(BaseApiView):
    def __init__(self):
        super(DmtcBill, self).__init__()
        self.model_class = Bill
        self.serializer_class = DmtcBillSerializer

    def post(self, request):
        return super(DmtcBill, self).post(request)

    def get(self, request):
        data = request.GET
        utils.check_tenant(data)
        return super(DmtcBill, self).get(request)


class DmtcBillOrder(BaseApiView):
    def __init__(self):
        super(DmtcBillOrder, self).__init__()
        self.model_class = BillOrder
        self.serializer_class = DmtcBillOrderSerializer

    def post(self, request):
        return super(DmtcBillOrder, self).post(request)

    def get(self, request):
        data = request.GET
        utils.check_tenant(data)
        return super(DmtcBillOrder, self).get(request)
