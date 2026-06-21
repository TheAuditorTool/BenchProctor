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

def BenchmarkTest45629(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = handle(cookie_value)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
