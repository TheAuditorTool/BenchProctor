# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import re


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest51095(request):
    xml_value = request.body.decode('utf-8')
    data = default_blank(xml_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    globals()['counter'] = int(processed)
    return JsonResponse({"saved": True})
