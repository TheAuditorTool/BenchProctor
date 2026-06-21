# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import json
import asyncio


_shared_counter_lock = threading.Lock()

def BenchmarkTest19716(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return graphql_var
    data = asyncio.run(fetch_payload())
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
