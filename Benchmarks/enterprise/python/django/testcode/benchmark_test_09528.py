# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest09528(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = handle(referer_value)
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
