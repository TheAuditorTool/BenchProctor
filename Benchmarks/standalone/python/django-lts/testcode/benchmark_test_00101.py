# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest00101(request):
    xml_value = request.body.decode('utf-8')
    parts = []
    for token in str(xml_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
