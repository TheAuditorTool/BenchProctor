# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import json


def BenchmarkTest00306(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data, _sep, _rest = str(json_value).partition('\x00')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
