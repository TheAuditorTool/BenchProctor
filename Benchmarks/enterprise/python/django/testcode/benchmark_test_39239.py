# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest39239(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = handle(referer_value)
    eval(compile('importlib.import_module(str(data))', '<sink>', 'exec'))
    return JsonResponse({"saved": True})
