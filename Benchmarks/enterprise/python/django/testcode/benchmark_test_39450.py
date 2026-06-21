# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from lxml import etree


def normalise_input(value):
    return value.strip()

def BenchmarkTest39450(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = normalise_input(origin_value)
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!\\[\\]-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return JsonResponse({"saved": True})
