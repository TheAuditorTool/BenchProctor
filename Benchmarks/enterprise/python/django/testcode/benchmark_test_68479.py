# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest68479(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(origin_value).encode(), _parser)
    return JsonResponse({"saved": True})
