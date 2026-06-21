# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import asyncio


def BenchmarkTest13440(request):
    raw_body = request.body.decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return raw_body
    data = asyncio.run(fetch_payload())
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
