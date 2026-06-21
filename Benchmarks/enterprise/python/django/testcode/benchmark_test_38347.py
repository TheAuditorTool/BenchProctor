# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json
import asyncio


def BenchmarkTest38347(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = asyncio.run(fetch_payload())
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
