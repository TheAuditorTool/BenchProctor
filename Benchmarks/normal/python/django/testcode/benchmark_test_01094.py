# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
from app_runtime import db


_shared_counter_lock = threading.Lock()

def BenchmarkTest01094(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = f'{db_value:.200s}'
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
