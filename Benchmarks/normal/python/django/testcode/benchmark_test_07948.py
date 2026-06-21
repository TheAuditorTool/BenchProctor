# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest07948(request):
    host_value = request.META.get('HTTP_HOST', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(host_value).encode(), _parser)
    return JsonResponse({"saved": True})
