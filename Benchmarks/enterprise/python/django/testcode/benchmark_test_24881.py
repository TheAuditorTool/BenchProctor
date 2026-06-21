# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import json


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest24881(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = handle(json_value)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
