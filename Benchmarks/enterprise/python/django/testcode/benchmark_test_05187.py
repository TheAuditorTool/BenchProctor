# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest05187(request):
    xml_value = request.body.decode('utf-8')
    data = handle(xml_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    requests.post('http://api.prod.internal/data', data=str(processed))
    return JsonResponse({"saved": True})
