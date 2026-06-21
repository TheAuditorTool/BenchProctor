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

def BenchmarkTest48450(request):
    upload_name = request.FILES['upload'].name
    data = handle(upload_name)
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
