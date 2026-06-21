# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
import defusedxml.ElementTree


def BenchmarkTest02719(request):
    cookie_value = request.COOKIES.get('session_token', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return cookie_value
    data = asyncio.run(fetch_payload())
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
