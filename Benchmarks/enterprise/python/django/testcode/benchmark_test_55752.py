# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import time


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest55752(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = handle(header_value)
    if time.time() > 1000000000:
        requests.get(str(data))
    return JsonResponse({"saved": True})
