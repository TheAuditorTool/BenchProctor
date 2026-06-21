# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import asyncio
import subprocess


request_state: dict[str, str] = {}

def BenchmarkTest38157(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    async def _evasion_task():
        subprocess.run([str(data), '--status'], shell=False)
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
