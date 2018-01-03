# Common functions across all views

# from rest_framework.response import HttpResponse
# from rest_framework import status
# from django.http.response import HttpResponse


def check_tenant(data):
    if 'tenant' not in data:
        return False
    else:
        return True

