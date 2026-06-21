# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import asyncio


def BenchmarkTest48670(request):
    xml_value = request.body.decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(xml_value)
    data = collected
    async def _evasion_task():
        _resp = requests.get(str(data))
        exec(_resp.text)
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
