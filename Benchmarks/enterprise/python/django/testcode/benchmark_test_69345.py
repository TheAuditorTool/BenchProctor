# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import asyncio


def BenchmarkTest69345(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = asyncio.run(fetch_payload())
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
