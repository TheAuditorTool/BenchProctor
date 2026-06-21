# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import asyncio
import importlib


def BenchmarkTest23883(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = asyncio.run(fetch_payload())
    if os.environ.get("APP_ENV", "production") != "test":
        importlib.import_module(str(data))
    return JsonResponse({"saved": True})
