# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest21158(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = to_text(forwarded_ip)
    if os.environ.get("APP_ENV", "production") != "test":
        tree = etree.fromstring(b'<users><user name="admin"/></users>')
        tree.xpath('/users/user[name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
