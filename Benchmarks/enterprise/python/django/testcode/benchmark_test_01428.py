# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re
import json


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest01428(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = handle(json_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
