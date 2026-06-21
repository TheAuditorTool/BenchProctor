# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest13811(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = default_blank(origin_value)
    processed = data[:64]
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return JsonResponse({"saved": True})
