# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


request_state: dict[str, str] = {}
_shared_counter_lock = threading.Lock()

def BenchmarkTest03462(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
