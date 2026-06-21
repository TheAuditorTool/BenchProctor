# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import json


_shared_counter_lock = threading.Lock()

def BenchmarkTest06664(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    try:
        data = json.loads(json_value).get('value', json_value)
    except (json.JSONDecodeError, AttributeError):
        data = json_value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
