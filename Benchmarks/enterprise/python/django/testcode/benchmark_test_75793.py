# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json
import asyncio


def BenchmarkTest75793(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
