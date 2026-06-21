# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import asyncio
import urllib.request


def BenchmarkTest01820(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
