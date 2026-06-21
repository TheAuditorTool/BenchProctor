# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import importlib
import sys


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest37403(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = handle(origin_value)
    if os.environ.get("APP_ENV", "production") != "test":
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
