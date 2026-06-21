# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest13361(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = handle(json_value)
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return JsonResponse({'error': 'file error'}, status=500)
    return JsonResponse({"saved": True})
