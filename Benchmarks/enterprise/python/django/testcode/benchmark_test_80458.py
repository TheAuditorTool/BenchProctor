# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


_shared_counter_lock = threading.Lock()

def BenchmarkTest80458(request, path_param):
    path_value = path_param
    with _shared_counter_lock:
        globals()['counter'] = int(path_value)
    return JsonResponse({"saved": True})
