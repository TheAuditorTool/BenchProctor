# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


request_state: dict[str, str] = {}
_shared_counter_lock = threading.Lock()

def BenchmarkTest08901(request):
    xml_value = request.body.decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
