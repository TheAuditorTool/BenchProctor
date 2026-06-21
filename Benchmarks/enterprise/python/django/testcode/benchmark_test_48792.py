# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


class RequestContext:
    def __init__(self, payload):
        self.payload = payload
_shared_counter_lock = threading.Lock()

def BenchmarkTest48792(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    ctx = RequestContext(origin_value)
    data = ctx.payload
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
