# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import asyncio


request_state: dict[str, str] = {}

def BenchmarkTest00445(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    async def _evasion_task():
        _resp = requests.get(str(data))
        exec(_resp.text)
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
