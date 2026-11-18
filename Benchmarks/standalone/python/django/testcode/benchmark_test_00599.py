# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest00599(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    parts = str(header_value).split(',')
    data = ' '.join(parts)
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
