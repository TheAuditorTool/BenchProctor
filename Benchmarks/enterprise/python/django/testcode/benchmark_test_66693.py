# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import asyncio


_shared_counter_lock = threading.Lock()

def BenchmarkTest66693(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = asyncio.run(fetch_payload())
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
