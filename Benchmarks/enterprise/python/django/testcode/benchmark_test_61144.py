# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import os


_shared_counter_lock = threading.Lock()

def BenchmarkTest61144(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
