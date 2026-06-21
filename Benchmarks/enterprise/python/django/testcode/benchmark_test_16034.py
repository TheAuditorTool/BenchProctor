# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import time
import runpy


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest16034(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = handle(json_value)
    if time.time() > 1000000000:
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
