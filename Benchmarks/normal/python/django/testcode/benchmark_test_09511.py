# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time
import asyncio
import importlib


def BenchmarkTest09511(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        importlib.import_module(str(data))
    return JsonResponse({"saved": True})
