# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest54922(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = handle(referer_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
