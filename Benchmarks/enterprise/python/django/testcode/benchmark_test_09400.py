# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest09400(request, path_param):
    path_value = path_param
    data = handle(path_value)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
