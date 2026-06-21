# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import ast


_shared_counter_lock = threading.Lock()

def BenchmarkTest01065(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
