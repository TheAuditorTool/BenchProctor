# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest69435(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = handle(json_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
