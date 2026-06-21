# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import asyncio


def BenchmarkTest58164(request):
    xml_value = request.body.decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = asyncio.run(fetch_payload())
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
