# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest23681(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = handle(referer_value)
    os.remove(str(data))
    return JsonResponse({"saved": True})
