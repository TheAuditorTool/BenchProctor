# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
import asyncio


def BenchmarkTest60582(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return dotenv_value
    data = asyncio.run(fetch_payload())
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
