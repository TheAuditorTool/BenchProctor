# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from lxml import etree


def BenchmarkTest60279(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(graphql_var).encode(), _parser)
    return JsonResponse({"saved": True})
