# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def relay_value(value):
    return value

def BenchmarkTest11692(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = relay_value(auth_header)
    processed = data[:64]
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return JsonResponse({"saved": True})
