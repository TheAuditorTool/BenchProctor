# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time
import asyncio
import importlib


def BenchmarkTest56664(request):
    raw_body = request.body.decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return raw_body
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        importlib.import_module(str(data))
    return JsonResponse({"saved": True})
