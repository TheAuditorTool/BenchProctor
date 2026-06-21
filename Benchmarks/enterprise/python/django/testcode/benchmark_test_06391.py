# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import asyncio


def BenchmarkTest06391(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
