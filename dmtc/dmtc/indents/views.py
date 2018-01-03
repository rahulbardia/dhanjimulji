# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from dmtc.users.views import BaseApiView
from dmtc import utils
# Model Imports
from models import Indents, IndentOrder, Transport, ConfirmationOrder

# Serializer Imports
from serializers import DmtcTransportSerializer, DmtcIndentSerializer, DmtcIndentOrderSerializer,\
    DmtcConfirmationOrderSerializer


class DmtcTransport(BaseApiView):
    """
    Handle all the transpoters
    Note: Transport is independent of tenants and user ids

    """

    def __init__(self):
        super(DmtcTransport, self).__init__()
        self.model_class = Transport
        self.serializer_class = DmtcTransportSerializer

        # def post(self, request):
        #     return super(DmtcTransport, self).post(request)
        #
        # def get(self, request):
        #     data = request.GET
        #     utils.check_tenant(data)
        #     return super(DmtcTransport, self).get(request)


class DmtcIndent(BaseApiView):
    """
    Handle indents at tenant level

    """

    def __init__(self):
        super(DmtcIndent, self).__init__()
        self.model_class = Indents
        self.serializer_class = DmtcIndentSerializer

    # def post(self, request):
    #     return super(DmtcIndent, self).post(request)

    def get(self, request):
        data = request.GET
        if not utils.check_tenant(data):
            return Response('No Tenant provided', status=status.HTTP_403_FORBIDDEN)
        return super(DmtcIndent, self).get(request)


class DmtcIndentOrder(BaseApiView):
    """
    Handle indents at tenant level

    """

    def __init__(self):
        super(DmtcIndentOrder, self).__init__()
        self.model_class = IndentOrder
        self.serializer_class = DmtcIndentOrderSerializer

    def get(self, request):
        data = request.GET
        if not utils.check_tenant(data):
            return Response('No Tenant provided', status=status.HTTP_403_FORBIDDEN)
        return super(DmtcIndentOrder, self).get(request)

# Code to return data for field

        # def post(self, request):
        #     return super(DmtcIndent, self).post(request)
        #
        # def reformat_data(self, obj):
        #     data = []
        #     for dic in obj:
        #         input_dic = dict()
        #         # Mandatory fields
        #         input_dic['tenant'] = dic['tenant']
        #         input_dic['indent'] = dic['indent']
        #         input_dic['packing'] = dic['supplier_inventory__packing']
        #         input_dic['cuts'] = dic['supplier_inventory__cuts']
        #         input_dic['quality'] = dic['supplier_inventory__quality']
        #         input_dic['size'] = dic['supplier_inventory__size']
        #         input_dic['rate'] = dic['supplier_inventory__rate']
        #         input_dic['sort_no'] = dic['supplier_inventory__sort_no']
        #         input_dic['item_name'] = dic['supplier_inventory__item_name']
        #         input_dic['supplier'] = dic['supplier_inventory__supplier__name']
        #         input_dic['bales'] = dic['bales']
        #         # Optional fields
        #         if 'sub_tenant' in dic:
        #             input_dic['sub_tenant'] = dic['sub_tenant']
        #         if 'supplier_inventory__description' in dic:
        #             input_dic['inventory_description'] = dic['supplier_inventory__description']
        #         if 'supplier_inventory__supplier_child__name' in dic:
        #             input_dic['supplier_child'] = dic['supplier_inventory__supplier_child__name']
        #         data.append(input_dic)
        #     return data
        #
        # def get(self, request):
        #     data = request.GET
        #     if not utils.check_tenant(data):
        #         return Response('No Tenant provided', status=status.HTTP_403_FORBIDDEN)
        #     # return super(DmtcIndentOrder, self).get(request)
        #     return_obj = self.model_class.objects.filter(**self.filter)\
        #         .select_related('supplier_inventory', 'supplier').values('tenant', 'sub_tenant', 'indent',
        #                                                                  'supplier_inventory__cuts',
        #                                                      'supplier_inventory__description',
        #                                                      'supplier_inventory__item_name',
        #                                                      'supplier_inventory__packing',
        #                                                      'supplier_inventory__quality',
        #                                                      'supplier_inventory__rate',
        #                                                      'supplier_inventory__size',
        #                                                      'supplier_inventory__sort_no',
        #                                                      'supplier_inventory__sub_tenant', 'bales', 'remarks',
        #                                                      'supplier_inventory__supplier__name',
        #                                                      'supplier_inventory__supplier_child__name')
        #     # return_obj.supplier_inventory_set.all()
        #     # print return_obj
        #     # for k in return_obj:
        #     #     # k = k.__dict__
        #     #     for key, v in k.iteritems():
        #     #         print key, v
        #     #         # if key == 'supplier_inventory_id':
        #     #         #     print "CUTS are", return_obj.supplier_inventory.cuts
        #     #     print ""
        #     data = self.reformat_data(return_obj)
        #     serializer = self.serializer_class(data, many=True)
        #     return Response(serializer.data)


class DmtcConfirmationOrder(BaseApiView):
    """
    Handle indents at tenant level

    """

    def __init__(self):
        super(DmtcConfirmationOrder, self).__init__()
        self.model_class = ConfirmationOrder
        self.serializer_class = DmtcConfirmationOrderSerializer

    def get(self, request):
        data = request.GET
        if not utils.check_tenant(data):
            return Response('No Tenant provided', status=status.HTTP_403_FORBIDDEN)
        return super(DmtcConfirmationOrder, self).get(request)