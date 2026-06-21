# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest22609(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = handle(origin_value)
    if time.time() > 1000000000:
        eval(str(data))
    return JsonResponse({"saved": True})
