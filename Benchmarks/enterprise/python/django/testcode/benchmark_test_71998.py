# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import json


def BenchmarkTest71998(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(json_value) + '"]')
    return JsonResponse({"saved": True})
