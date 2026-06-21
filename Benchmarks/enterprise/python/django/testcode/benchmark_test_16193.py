# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import time


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest16193(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = handle(host_value)
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
