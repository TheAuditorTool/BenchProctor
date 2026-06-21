# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import os
from types import SimpleNamespace


def BenchmarkTest49061(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        tree = etree.fromstring(b'<users><user name="admin"/></users>')
        tree.xpath('/users/user[name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
