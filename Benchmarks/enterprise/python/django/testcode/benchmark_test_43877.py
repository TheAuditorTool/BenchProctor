# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import asyncio


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest43877(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    ctx = RequestContext(origin_value)
    data = ctx.payload
    async def _evasion_task():
        requests.get(str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
