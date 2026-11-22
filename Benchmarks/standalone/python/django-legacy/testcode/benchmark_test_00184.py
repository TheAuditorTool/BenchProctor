# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import json


def BenchmarkTest00184(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    parts = []
    for token in str(json_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    find_user = etree.XPath('/users/user[@name="' + str(data) + '"]')
    find_user(tree)
    return JsonResponse({"saved": True})
