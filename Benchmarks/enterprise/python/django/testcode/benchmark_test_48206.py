# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest48206(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
