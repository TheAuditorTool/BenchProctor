# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest03932(request):
    xml_value = request.body.decode('utf-8')
    ctx = RequestContext(xml_value)
    data = ctx.payload
    async def _evasion_task():
        eval(str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
