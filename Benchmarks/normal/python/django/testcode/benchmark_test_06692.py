# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


class RequestContext:
    def __init__(self, payload):
        self.payload = payload
_shared_counter_lock = threading.Lock()

def BenchmarkTest06692(request):
    raw_body = request.body.decode('utf-8')
    ctx = RequestContext(raw_body)
    data = ctx.payload
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
