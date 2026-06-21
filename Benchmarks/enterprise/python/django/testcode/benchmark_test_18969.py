# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


def ensure_str(value):
    return str(value)

def BenchmarkTest18969(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = ensure_str(header_value)
    async def _evasion_task():
        eval(str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
