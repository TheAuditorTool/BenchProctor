# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import os


_shared_counter_lock = threading.Lock()

def BenchmarkTest11771(request):
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
