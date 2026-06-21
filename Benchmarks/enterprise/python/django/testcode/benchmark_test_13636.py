# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest13636(request):
    host_value = request.META.get('HTTP_HOST', '')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(host_value) + '"]')
    return JsonResponse({"saved": True})
