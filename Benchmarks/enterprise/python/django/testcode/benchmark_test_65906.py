# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


def BenchmarkTest65906(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = asyncio.run(fetch_payload())
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
