# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


_shared_counter_lock = threading.Lock()

def BenchmarkTest81457(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
