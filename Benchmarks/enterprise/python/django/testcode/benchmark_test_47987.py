# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


def BenchmarkTest47987(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = asyncio.run(fetch_payload())
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
