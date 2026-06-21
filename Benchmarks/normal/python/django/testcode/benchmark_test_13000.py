# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
import asyncio


def BenchmarkTest13000(request):
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    requests.post('http://api.prod.internal/data', data=str(processed))
    return JsonResponse({"saved": True})
