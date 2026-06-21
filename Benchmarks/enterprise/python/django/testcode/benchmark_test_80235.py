# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import os
import json


_shared_counter_lock = threading.Lock()

def BenchmarkTest80235(request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
