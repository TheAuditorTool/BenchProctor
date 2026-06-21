# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest22661(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = handle(ua_value)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
