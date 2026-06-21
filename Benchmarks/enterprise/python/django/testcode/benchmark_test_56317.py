# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import asyncio
from app_runtime import db


_shared_counter_lock = threading.Lock()

def BenchmarkTest56317(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = asyncio.run(fetch_payload())
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
