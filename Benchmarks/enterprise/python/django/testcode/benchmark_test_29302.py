# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import os
import ast


_shared_counter_lock = threading.Lock()

def BenchmarkTest29302(request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
