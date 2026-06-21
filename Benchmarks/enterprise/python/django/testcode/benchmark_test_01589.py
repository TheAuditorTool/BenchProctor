# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from types import SimpleNamespace


def BenchmarkTest01589(request):
    xml_value = request.body.decode('utf-8')
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(processed))
    return JsonResponse({"saved": True})
