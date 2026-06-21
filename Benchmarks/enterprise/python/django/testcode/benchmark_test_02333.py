# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import urllib.request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest02333(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = handle(json_value)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
