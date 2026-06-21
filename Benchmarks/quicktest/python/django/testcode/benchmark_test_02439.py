# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


request_state: dict[str, str] = {}
_shared_counter_lock = threading.Lock()

def BenchmarkTest02439(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
