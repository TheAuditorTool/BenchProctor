# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
from app_runtime import db


_shared_counter_lock = threading.Lock()

def BenchmarkTest78415(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '%s' % (db_value,)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
