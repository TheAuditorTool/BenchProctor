# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import asyncio


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest53746(request):
    cookie_value = request.COOKIES.get('session_token', '')
    ctx = RequestContext(cookie_value)
    data = ctx.payload
    async def _evasion_task():
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
