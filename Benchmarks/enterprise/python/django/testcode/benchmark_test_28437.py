# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


_shared_counter_lock = threading.Lock()

def BenchmarkTest28437(request):
    cookie_value = request.COOKIES.get('session_token', '')
    with _shared_counter_lock:
        globals()['counter'] = int(cookie_value)
    return JsonResponse({"saved": True})
