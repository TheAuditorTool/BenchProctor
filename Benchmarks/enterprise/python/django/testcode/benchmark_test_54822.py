# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def normalise_input(value):
    return value.strip()
_shared_counter_lock = threading.Lock()

def BenchmarkTest54822(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = normalise_input(cookie_value)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
