# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import asyncio
import importlib


request_state: dict[str, str] = {}

def BenchmarkTest62087(request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    async def _evasion_task():
        importlib.import_module(str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
