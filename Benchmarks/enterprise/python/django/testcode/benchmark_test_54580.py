# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace
from lxml import etree


def BenchmarkTest54580(request):
    xml_value = request.body.decode('utf-8')
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    eval(compile('_parser = etree.XMLParser(resolve_entities=True, no_network=False)\netree.fromstring(str(data).encode(), _parser)', '<sink>', 'exec'))
    return JsonResponse({"saved": True})
