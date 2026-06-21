# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()
_shared_counter_lock = threading.Lock()

def BenchmarkTest48598(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = handle(host_value)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
