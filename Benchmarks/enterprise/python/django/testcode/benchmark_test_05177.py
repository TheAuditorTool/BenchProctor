# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


def BenchmarkTest05177(request):
    cookie_value = request.COOKIES.get('session_token', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return cookie_value
    data = asyncio.run(fetch_payload())
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
