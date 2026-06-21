# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import importlib


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest11045(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = handle(referer_value)
    if os.environ.get("APP_ENV", "production") != "test":
        importlib.import_module(str(data))
    return JsonResponse({"saved": True})
