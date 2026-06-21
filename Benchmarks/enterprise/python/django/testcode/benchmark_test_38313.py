# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
import pickle


request_state: dict[str, str] = {}

def BenchmarkTest38313(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    async def _evasion_task():
        pickle.loads(data.encode('latin-1'))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
