# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from lxml import etree


def ensure_str(value):
    return str(value)

def BenchmarkTest71799(request):
    upload_name = request.FILES['upload'].name
    data = ensure_str(upload_name)
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!\\[\\]-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return JsonResponse({"saved": True})
