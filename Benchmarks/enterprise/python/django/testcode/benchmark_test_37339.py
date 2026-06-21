# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest37339(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = handle(json_value)
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
