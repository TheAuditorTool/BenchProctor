# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time
import asyncio


def BenchmarkTest18154(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        eval(str(data))
    return JsonResponse({"saved": True})
