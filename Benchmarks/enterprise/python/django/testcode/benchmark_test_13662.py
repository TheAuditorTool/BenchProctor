# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


request_state: dict[str, str] = {}

def BenchmarkTest13662(request):
    upload_name = request.FILES['upload'].name
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    async def _evasion_task():
        eval(str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
