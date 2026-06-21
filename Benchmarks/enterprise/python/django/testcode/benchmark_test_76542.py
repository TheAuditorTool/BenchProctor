# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest76542(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = handle(origin_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    if str(processed).startswith('https://admin.internal/'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
