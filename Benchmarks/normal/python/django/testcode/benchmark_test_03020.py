# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import asyncio
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest03020(request):
    raw_body = request.body.decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return raw_body
    data = asyncio.run(fetch_payload())
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
