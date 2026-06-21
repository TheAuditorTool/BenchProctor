# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
import asyncio


def BenchmarkTest59182(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    os.remove(str(data))
    return JsonResponse({"saved": True})
