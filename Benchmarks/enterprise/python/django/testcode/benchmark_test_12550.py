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

def BenchmarkTest12550(request):
    user_id = request.GET.get('id', '')
    data = handle(user_id)
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
