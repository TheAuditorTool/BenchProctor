# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def to_text(value):
    return str(value).strip()

def BenchmarkTest30398(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = to_text(auth_header)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
