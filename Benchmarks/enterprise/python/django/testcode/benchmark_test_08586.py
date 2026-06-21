# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from lxml import etree


def BenchmarkTest08586(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = f'{json_value}'
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return JsonResponse({"saved": True})
