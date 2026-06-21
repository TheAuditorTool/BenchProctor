# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest14098(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = handle(auth_header)
    processed = data[:64]
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return JsonResponse({"saved": True})
