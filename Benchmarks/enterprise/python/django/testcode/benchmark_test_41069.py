# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time
from types import SimpleNamespace
from lxml import etree


def BenchmarkTest41069(request):
    raw_body = request.body.decode('utf-8')
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    return JsonResponse({"saved": True})
