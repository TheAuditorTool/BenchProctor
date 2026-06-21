# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
from types import SimpleNamespace


_shared_counter_lock = threading.Lock()

def BenchmarkTest01024(request):
    upload_name = request.FILES['upload'].name
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
