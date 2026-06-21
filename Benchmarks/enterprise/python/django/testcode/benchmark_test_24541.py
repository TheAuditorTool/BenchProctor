# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import asyncio


def BenchmarkTest24541(request):
    cookie_value = request.COOKIES.get('session_token', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return cookie_value
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    yaml.load(processed, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
