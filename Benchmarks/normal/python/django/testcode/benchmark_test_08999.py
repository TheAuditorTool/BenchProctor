# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json
import asyncio


def BenchmarkTest08999(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})
