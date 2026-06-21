# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest07849(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        tree = etree.fromstring(b'<users><user name="admin"/></users>')
        tree.xpath('/users/user[name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
