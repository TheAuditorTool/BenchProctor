# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest46406(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
