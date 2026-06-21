# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


def BenchmarkTest72055(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return ua_value
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    exec(str(processed))
    return JsonResponse({"saved": True})
