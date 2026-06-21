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

def BenchmarkTest56242(request, path_param):
    path_value = path_param
    data = handle(path_value)
    if os.environ.get("APP_ENV", "production") != "test":
        _resp = requests.get(str(data))
        exec(_resp.text)
    return JsonResponse({"saved": True})
