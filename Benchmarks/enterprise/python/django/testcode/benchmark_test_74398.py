# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest74398(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = handle(origin_value)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
