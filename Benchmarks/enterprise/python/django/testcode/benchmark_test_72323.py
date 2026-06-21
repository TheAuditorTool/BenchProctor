# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
import importlib


def BenchmarkTest72323(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = asyncio.run(fetch_payload())
    async def _evasion_task():
        importlib.import_module(str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
