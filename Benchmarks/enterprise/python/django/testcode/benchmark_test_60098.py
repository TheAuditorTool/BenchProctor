# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest60098(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})
