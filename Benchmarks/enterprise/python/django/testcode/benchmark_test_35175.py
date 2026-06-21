# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import asyncio


request_state: dict[str, str] = {}

def BenchmarkTest35175(request):
    raw_body = request.body.decode('utf-8')
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    async def _evasion_task():
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
