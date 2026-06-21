# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest04591(request, path_param):
    path_value = path_param
    data = handle(path_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
