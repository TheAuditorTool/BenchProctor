# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload
_shared_counter_lock = threading.Lock()

def BenchmarkTest03089(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ctx = RequestContext(comment_value)
    data = ctx.payload
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
