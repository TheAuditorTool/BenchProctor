# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest44226(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = handle(origin_value)
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
