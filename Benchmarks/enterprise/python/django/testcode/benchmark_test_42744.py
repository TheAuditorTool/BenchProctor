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

def BenchmarkTest42744(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = handle(graphql_var)
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
