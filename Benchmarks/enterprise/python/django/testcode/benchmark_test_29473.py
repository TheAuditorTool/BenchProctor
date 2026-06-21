# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest29473(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(header_value).encode(), _parser)
    return JsonResponse({"saved": True})
