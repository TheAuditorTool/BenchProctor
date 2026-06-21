# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest76321(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = handle(origin_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
