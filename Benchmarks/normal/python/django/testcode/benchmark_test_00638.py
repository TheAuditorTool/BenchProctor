# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest00638(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    processed = 'true' if str(auth_header).lower() in ('true', '1', 'yes', 'on') else 'false'
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
