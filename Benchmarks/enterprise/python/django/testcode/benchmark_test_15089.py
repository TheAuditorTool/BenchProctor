# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()
_shared_counter_lock = threading.Lock()

def BenchmarkTest15089(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
