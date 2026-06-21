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

def BenchmarkTest07538(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = handle(origin_value)
    if os.environ.get("APP_ENV", "production") != "test":
        requests.get(str(data))
    return JsonResponse({"saved": True})
