# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest23511(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
