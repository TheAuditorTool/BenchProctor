# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import json


def to_text(value):
    return str(value).strip()

def BenchmarkTest05816(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = to_text(json_value)
    processed = data[:64]
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
