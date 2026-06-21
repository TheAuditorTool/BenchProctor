# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import time
import asyncio


def BenchmarkTest14431(request):
    xml_value = request.body.decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        requests.get(str(data))
    return JsonResponse({"saved": True})
