# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


def BenchmarkTest36932(request, path_param):
    path_value = path_param
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = asyncio.run(fetch_payload())
    int(str(data))
    return JsonResponse({"saved": True})
