# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import asyncio


_shared_counter_lock = threading.Lock()

def BenchmarkTest12541(request):
    multipart_value = request.POST.get('multipart_field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return multipart_value
    data = asyncio.run(fetch_payload())
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
