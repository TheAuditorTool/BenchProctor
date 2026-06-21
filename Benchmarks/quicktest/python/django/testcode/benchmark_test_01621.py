# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import os


_shared_counter_lock = threading.Lock()

def BenchmarkTest01621(request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
