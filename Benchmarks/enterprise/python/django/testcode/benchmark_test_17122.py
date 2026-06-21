# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json
import asyncio


def relay_value(value):
    return value

def BenchmarkTest17122(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = relay_value(json_value)
    async def _evasion_task():
        _resp = requests.get(str(data))
        exec(_resp.text)
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
