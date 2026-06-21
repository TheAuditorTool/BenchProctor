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

def BenchmarkTest28083(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = handle(json_value)
    os.remove(str(data))
    return JsonResponse({"saved": True})
