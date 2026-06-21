# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time
import runpy


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest59291(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = handle(referer_value)
    if time.time() > 1000000000:
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
