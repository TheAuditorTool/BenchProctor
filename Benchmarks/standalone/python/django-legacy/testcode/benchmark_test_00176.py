# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import json


def BenchmarkTest00176(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data = str(json_value).replace('\x00', '')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    etree.XPathEvaluator(tree)('/users/user[@name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
