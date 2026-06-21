# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest64557(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(auth_header).encode(), _parser)
    return JsonResponse({"saved": True})
