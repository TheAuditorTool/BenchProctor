# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time
import importlib


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest73973(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = handle(ua_value)
    if time.time() > 1000000000:
        importlib.import_module(str(data))
    return JsonResponse({"saved": True})
