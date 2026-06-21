# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
import requests


def BenchmarkTest04692(request):
    user_id = request.GET.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = asyncio.run(fetch_payload())
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
