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

def BenchmarkTest63221(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = handle(forwarded_ip)
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
