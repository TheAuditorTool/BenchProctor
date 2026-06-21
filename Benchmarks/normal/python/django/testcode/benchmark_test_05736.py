# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json
import asyncio


def BenchmarkTest05736(request, path_param):
    path_value = path_param
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = asyncio.run(fetch_payload())
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
