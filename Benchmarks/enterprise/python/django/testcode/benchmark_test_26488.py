# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
from types import SimpleNamespace


_shared_counter_lock = threading.Lock()

def BenchmarkTest26488(request, path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
