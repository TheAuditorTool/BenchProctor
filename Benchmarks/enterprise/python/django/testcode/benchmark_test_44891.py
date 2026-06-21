# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from lxml import etree


def BenchmarkTest44891(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = str(json_value).replace('\x00', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return JsonResponse({"saved": True})
