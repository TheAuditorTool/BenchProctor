# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest32537(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = handle(referer_value)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
