# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login

# Models
from models import BaseModel, Tenant, DmtcUser, Buyer, Supplier, SupplierInventory,\
    Salesman

# Serializers
from serializers import BaseSerializer, TenantSerializer, DmtcUserSerializer,\
    DmtcBuyerSerializer, DmtcSupplierSerializer, DmtcSupplierInventorySerializer,\
    DmtcSalesmanSerializer, LoginSerializer

# My Libs
from dmtc import utils

# Std Libs
import json

# Create your views here.


class BaseApiView(APIView):

    def __init__(self):
        APIView.__init__(self)
        self.model_class = BaseModel
        self.serializer_class = BaseSerializer
        self.filter_list = []
        self.filter = {}

    def post(self, request):
        data = request.body
        tenant_provided = utils.check_tenant(data)
        data = json.loads(data)
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        print serializer.errors
        return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)

    def get(self, request):
        # Only accept first tenant, so no matter what user cannot see data of more than one tenant
        return_obj = self.model_class.objects.filter(**self.filter)
        serializer = self.serializer_class(return_obj, many=True)
        return Response(serializer.data)

    def create_filter(self, data):
        for key in self.filter_list:
            if key in data:
                # For tenant always get only 1 tenant id
                if type(data.getlist(key)) == list and key != 'tenant':
                    self.filter[key+'__in'] = data.getlist(key)
                else:
                    self.filter[key] = data[key]


class DmtcTenant(BaseApiView):
    """
    Get tenant Information

    """
    def get(self, request):
        tenant_obj = Tenant.objects.all()
        serializer = TenantSerializer(tenant_obj, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = TenantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DmtcLogin(BaseApiView):
    """
    dmtc user login
    When creating a user using Django Admin, also use post API
    to make an entry for Dmtc User to assign tenant/Sub-tenant
    to a USER.

    TBD

    """
# Custom login

    # def get(self, request):
    #     data = request.GET
    #     print "HEYHEYHEY"
    #     print data['tenant']
    #     try:
    #         user_obj = User.objects.filter(tenant_id=data['tenant']).values()[0]
    #         print user_obj
    #         print user_obj['id'], type(user_obj['id'])
    #         # for k,v in user_obj:
    #         #     print k, v ,"LALALALA"
    #         dmtc_user_obj = DmtcUser.objects.filter(user_id=user_obj['id']).values()[0]
    #         user_tenant = dmtc_user_obj['tenant_id']
    #         print int(user_tenant)
    #         serializer = DmtcUserSerializer(data=dmtc_user_obj)
    #
    #         return Response(utils.set_cookies(serializer.initial_data, 'tenant', user_tenant))
    #     except Exception as e:
    #         print e
    #         return Response(status=401)

# Django std login

    def get(self, request):
        username = request.GET['username']
        password = request.GET['password']
        print username, password
        user = authenticate(request, username=username, password=password)
        print user.id, "user id"
        if user is not None:
            login(request, user)
            dmtc_user_obj = DmtcUser.objects.filter(user_id=user.id)
            print dmtc_user_obj
            # print dmtc_user_obj.id
            # Redirect to a success page.
            return Response(dmtc_user_obj[0].tenant_id)
        else:
            print "Oops"

    def post(self, request):
        data = request.POST
        print data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DmtcTenantUser(BaseApiView):
    """
    dmtc tenant users information

    """
    def get(self, request):
        data = request.GET
        # if 'tenant' not in data:
        #     return Response('No tentant passed', status=status.HTTP_400_BAD_REQUEST)
        tenant = data['tenant'] if 'tenant' in data else None
        if tenant:
            tenant_obj = Tenant.objects.filer(id=tenant)
        else:
            tenant_obj = Tenant.objects.all()
        user_obj = User()

    def post(self, request):
        """
        Post user data for a given tenant
        :param request: Input request form
        :return: status
        """
        data = request.POST
        utils.check_tenant(data)
        try:
            user = User()
            user.first_name = data.get('first_name', None)
            user.last_name = data.get('last_name', None)
            if 'username' not in data:
                return Response('username necessary', status=status.HTTP_400_BAD_REQUEST)
            else:
                user.username = data.get('username')
            user.email = data.get('email', None)
            user.set_password(data.get('password', 'password'))
            user.save()
        except Exception as e:
            print(e, 'cannot save user')
            raise e
        dmtc_user = {}
        tenant_obj = Tenant.objects.filter(id=int(data['tenant']))
        dmtc_user['tenant'] = tenant_obj[0].id
        dmtc_user['user'] = user.id
        if 'place' not in data:
            return Response('place necessary', status=status.HTTP_400_BAD_REQUEST)
        else:
            dmtc_user['place'] = data.get('place')
        dmtc_user['address'] = data.get('address', None)
        dmtc_user['mobile_no'] = data.get('mobile_no', None)
        dmtc_user['email'] = data.get('email', None)
        dmtc_user['is_admin'] = data.get('is_admin', False)
        print(dmtc_user)
        serializer = DmtcUserSerializer(data=dmtc_user)
        if serializer.is_valid():
            print("It is valid")
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_304_NOT_MODIFIED)


class DmtcBuyer(BaseApiView):
    """
    Tenant level Buyer information

    """
    def __init__(self):
        super(DmtcBuyer, self).__init__()
        self.serializer_class = DmtcBuyerSerializer
        self.model_class = Buyer

    def post(self, request):
        return super(DmtcBuyer, self).post(request)

    def get(self, request):
        data = request.GET
        if not utils.check_tenant(data):
            return Response('No Tenant provided', status=status.HTTP_403_FORBIDDEN)
        return super(DmtcBuyer, self).get(request)


class DmtcSupplier(BaseApiView):
    """
    Tenant level Supplier Information

    """
    def __init__(self):
        super(DmtcSupplier, self).__init__()
        self.serializer_class = DmtcSupplierSerializer
        self.model_class = Supplier

    # def post(self, request):
    #     return super(DmtcSupplier, self).post(request)

    def get(self, request):
        data = request.GET
        if not utils.check_tenant(data):
            return Response('No Tenant provided', status=status.HTTP_403_FORBIDDEN)
        return super(DmtcSupplier, self).get(request)


class DmtcSupplierInventory(BaseApiView):
    """
    Handle the Inventory for an supplier

    """
    def __init__(self):
        super(DmtcSupplierInventory, self).__init__()
        self.serializer_class = DmtcSupplierInventorySerializer
        self.model_class = SupplierInventory
        self.filter_list = ['tenant', 'quality', 'item_name',
                            'sort_no', 'packing', 'size', 'rate_gt', 'rate_lt']

    # def post(self, request):
    #     return super(DmtcSupplierInventory, self).post(request)

    def get(self, request):
        data = request.GET
        if not utils.check_tenant(data):
            return Response('No Tenant provided', status=status.HTTP_403_FORBIDDEN)
        self.create_filter(data)
        return super(DmtcSupplierInventory, self).get(request)


class DmtcSalesman(BaseApiView):
    """
    Handle the Salesman Information for tenant

    """
    def __init__(self):
        super(DmtcSalesman, self).__init__()
        self.serializer_class = DmtcSalesmanSerializer
        self.model_class = Salesman

    # def post(self, request):
    #     return super(DmtcSalesman, self).post(request)
    #
    def get(self, request):
        data = request.GET
        if not utils.check_tenant(data):
            return Response('No Tenant provided', status=status.HTTP_403_FORBIDDEN)
        return super(DmtcSalesman, self).get(request)
