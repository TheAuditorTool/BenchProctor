# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json
import asyncio
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest74623(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
