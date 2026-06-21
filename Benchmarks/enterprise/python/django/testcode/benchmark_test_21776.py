# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from lxml import etree


def BenchmarkTest21776(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(json_value).encode(), _parser)
    return JsonResponse({"saved": True})
