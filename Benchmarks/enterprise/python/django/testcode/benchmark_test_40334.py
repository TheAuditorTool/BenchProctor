# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
from app_runtime import db


_shared_counter_lock = threading.Lock()

def BenchmarkTest40334(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    with _shared_counter_lock:
        globals()['counter'] = int(comment_value)
    return JsonResponse({"saved": True})
