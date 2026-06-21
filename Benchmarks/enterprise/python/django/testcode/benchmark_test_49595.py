# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import socket


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest49595(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    processed = data[:64]
    s = socket.create_connection((str(processed), 80))
    s.close()
    return JsonResponse({"saved": True})
