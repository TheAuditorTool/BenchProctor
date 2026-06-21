# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse
import asyncio


request_state: dict[str, str] = {}

def BenchmarkTest41267(request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    async def _evasion_task():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return HttpResponse(content)
    return asyncio.run(_evasion_task())
