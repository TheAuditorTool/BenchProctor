# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time
import importlib
import sys


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest03781(request):
    raw_body = request.body.decode('utf-8')
    data = handle(raw_body)
    if time.time() > 1000000000:
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
