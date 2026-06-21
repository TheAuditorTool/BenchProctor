# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
import runpy


request_state: dict[str, str] = {}

def BenchmarkTest39577(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    async def _evasion_task():
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
