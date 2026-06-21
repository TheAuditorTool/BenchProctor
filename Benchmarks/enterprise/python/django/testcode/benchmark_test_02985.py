# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest02985(request):
    raw_body = request.body.decode('utf-8')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(raw_body).encode(), _parser)
    return JsonResponse({"saved": True})
