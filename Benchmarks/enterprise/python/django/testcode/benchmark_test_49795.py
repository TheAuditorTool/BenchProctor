# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def coalesce_blank(value):
    return value or ''

def BenchmarkTest49795(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = coalesce_blank(origin_value)
    def _primary():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
