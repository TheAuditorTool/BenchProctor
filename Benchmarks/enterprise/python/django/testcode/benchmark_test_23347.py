# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


request_state: dict[str, str] = {}

def BenchmarkTest23347(request):
    cookie_value = request.COOKIES.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    async def _evasion_task():
        eval(str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
