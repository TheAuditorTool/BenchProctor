# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


def BenchmarkTest66152(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = asyncio.run(fetch_payload())
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
