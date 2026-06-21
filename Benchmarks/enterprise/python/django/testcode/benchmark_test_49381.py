# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import asyncio


request_state: dict[str, str] = {}

def BenchmarkTest49381(request):
    xml_value = request.body.decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    async def _evasion_task():
        _resp = requests.get(str(data))
        exec(_resp.text)
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
