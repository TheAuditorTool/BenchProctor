# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def normalise_input(value):
    return value.strip()

def BenchmarkTest16074(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = normalise_input(referer_value)
    def _primary():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
