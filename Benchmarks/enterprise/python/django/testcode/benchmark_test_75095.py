# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest75095(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = ' '.join(str(header_value).split())
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return JsonResponse({"saved": True})
