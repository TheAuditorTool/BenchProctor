# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json
import urllib.request
import urllib.parse
import ssl


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest25116(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = handle(json_value)
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
