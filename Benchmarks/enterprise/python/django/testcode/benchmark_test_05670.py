# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import os
from types import SimpleNamespace


def BenchmarkTest05670(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    ns = SimpleNamespace(payload=forwarded_ip)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        tree = etree.fromstring(b'<users><user name="admin"/></users>')
        tree.xpath('/users/user[name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
