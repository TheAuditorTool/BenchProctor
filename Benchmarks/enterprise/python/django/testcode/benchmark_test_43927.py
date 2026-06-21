# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
from types import SimpleNamespace


_shared_counter_lock = threading.Lock()

def BenchmarkTest43927(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
