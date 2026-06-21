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

def BenchmarkTest01151(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = handle(json_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})
