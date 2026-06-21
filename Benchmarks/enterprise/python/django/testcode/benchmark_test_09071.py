# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import asyncio


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest09071(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = default_blank(referer_value)
    async def _evasion_task():
        requests.get(str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
