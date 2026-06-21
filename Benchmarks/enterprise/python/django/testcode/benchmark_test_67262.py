# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
import time


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest67262(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    if time.time() > 1000000000:
        requests.get(str(data))
    return JsonResponse({"saved": True})
