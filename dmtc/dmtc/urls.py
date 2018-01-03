"""dmtc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

# User Views
from dmtc.users.views import DmtcTenant, DmtcTenantUser, DmtcBuyer, \
    DmtcSupplier, DmtcSupplierInventory, DmtcSalesman

# Indent Views
from dmtc.indents.views import DmtcTransport, DmtcIndent, DmtcIndentOrder, DmtcConfirmationOrder

# Billing Views
from dmtc.billing.views import DmtcBill, DmtcBillOrder

# admin level urls

urlpatterns_admin = [
    url(r'^admin/', admin.site.urls),
]


# user level urls

urlpatterns_user = [
    url(r'^users/tenant/', DmtcTenant.as_view()),
    url(r'^users/user/$', DmtcTenantUser.as_view()),
    url(r'^users/buyer/$', DmtcBuyer.as_view()),
    url(r'^users/supplier/$', DmtcSupplier.as_view()),
    url(r'^users/supplierinventory/$', DmtcSupplierInventory.as_view()),
    url(r'^users/salesman/$', DmtcSalesman.as_view()),
]

# Indent level urls

urlpatterns_tenant = [
    url(r'^indent/transport/', DmtcTransport.as_view()),
    url(r'^indent/indents/', DmtcIndent.as_view()),
    url(r'^indent/indentsorder/', DmtcIndentOrder.as_view()),
    url(r'^indent/confirmationorder/', DmtcConfirmationOrder.as_view()),
]

# Billing level urls

urlpatterns_billing = [
    url(r'^billing/bill/', DmtcBill.as_view()),
    url(r'^billing/billorder/', DmtcBillOrder.as_view()),
]

# Accounting level urls

urlpatterns_accounting = []

# final url patterns
urlpatterns = urlpatterns_admin + urlpatterns_user + urlpatterns_tenant \
              + urlpatterns_billing + urlpatterns_accounting \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)