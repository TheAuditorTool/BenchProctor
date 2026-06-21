# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import json


_shared_counter_lock = threading.Lock()

def BenchmarkTest12182(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    with _shared_counter_lock:
        globals()['counter'] = int(json_value)
    return JsonResponse({"saved": True})
