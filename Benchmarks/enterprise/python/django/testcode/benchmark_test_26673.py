# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def ensure_str(value):
    return str(value)
_shared_counter_lock = threading.Lock()

def BenchmarkTest26673(request, path_param):
    path_value = path_param
    data = ensure_str(path_value)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
