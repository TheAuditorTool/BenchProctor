# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import asyncio


_shared_counter_lock = threading.Lock()

def BenchmarkTest41914(request):
    xml_value = request.body.decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = asyncio.run(fetch_payload())
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
