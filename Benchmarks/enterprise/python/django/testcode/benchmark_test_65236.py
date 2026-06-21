# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import asyncio


request_state: dict[str, str] = {}

def BenchmarkTest65236(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    async def _evasion_task():
        os.system('echo ' + str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
