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

def BenchmarkTest15121(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = handle(header_value)
    eval(compile("subprocess.Popen('echo ' + str(data), shell=True).wait()", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
