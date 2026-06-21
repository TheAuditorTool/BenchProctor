# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import asyncio


def BenchmarkTest18508(request):
    cookie_value = request.COOKIES.get('session_token', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return cookie_value
    data = asyncio.run(fetch_payload())
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
