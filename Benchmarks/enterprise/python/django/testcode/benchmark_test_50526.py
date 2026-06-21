# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import asyncio


_shared_counter_lock = threading.Lock()

def BenchmarkTest50526(request, path_param):
    path_value = path_param
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = asyncio.run(fetch_payload())
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
