# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import ast


_shared_counter_lock = threading.Lock()

def BenchmarkTest54809(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
