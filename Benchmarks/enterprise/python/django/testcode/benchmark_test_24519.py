# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import asyncio
import socket


def BenchmarkTest24519(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    async def _evasion_task():
        s = socket.create_connection((str(data), 80))
        s.close()
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
