# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import json


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest13037(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = default_blank(json_value)
    processed = data[:64]
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
