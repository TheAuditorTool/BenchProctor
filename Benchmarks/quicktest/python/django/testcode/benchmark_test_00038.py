# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest00038(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = handle(referer_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
