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

def BenchmarkTest24255(request):
    user_id = request.GET.get('id', '')
    data = handle(user_id)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
