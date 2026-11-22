# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from lxml import etree


def BenchmarkTest00118(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data = (lambda v: v.strip())(json_value)
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return JsonResponse({"saved": True})
