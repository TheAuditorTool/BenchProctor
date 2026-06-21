# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


def ensure_str(value):
    return str(value)

def BenchmarkTest12549(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ensure_str(ua_value)
    async def _evasion_task():
        eval(str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
