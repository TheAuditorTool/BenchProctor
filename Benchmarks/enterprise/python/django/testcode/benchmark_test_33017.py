# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest33017(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = handle(json_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
