# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import asyncio


request_state: dict[str, str] = {}

def BenchmarkTest61714(request):
    host_value = request.META.get('HTTP_HOST', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    async def _evasion_task():
        requests.get(str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
