# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import json


request_state: dict[str, str] = {}
_shared_counter_lock = threading.Lock()

def BenchmarkTest12973(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
