# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from lxml import etree


def BenchmarkTest00159(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    kind = 'json' if str(json_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(json_value).strip()
        case _:
            data = str(json_value)
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return JsonResponse({"saved": True})
