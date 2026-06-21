# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import os


_shared_counter_lock = threading.Lock()

def BenchmarkTest79818(request):
    env_value = os.environ.get('USER_INPUT', '')
    with _shared_counter_lock:
        globals()['counter'] = int(env_value)
    return JsonResponse({"saved": True})
