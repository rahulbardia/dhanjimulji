# Common functions across all views

# from rest_framework.response import HttpResponse
# from rest_framework import status
# from django.http.response import HttpResponse

import datetime
from django.conf import settings

def check_tenant(data):
    if 'tenant' not in data:
        return False
    else:
        return True


def get_request_data(data):
    print type(data.keys()[0])
    return data.keys()[0]


def set_cookie(response, key, value, days_expire=7):
    print "Inside set cookies in utils"
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  #one year
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(datetime.datetime.utcnow() +
                                         datetime.timedelta(seconds=max_age),
                                         "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie(key, value, max_age=max_age, expires=expires,
                        secure=settings.SESSION_COOKIE_SECURE or None)
