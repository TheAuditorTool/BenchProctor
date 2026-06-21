# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import time


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest68556(request):
    xml_value = request.body.decode('utf-8')
    data = handle(xml_value)
    if time.time() > 1000000000:
        yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
