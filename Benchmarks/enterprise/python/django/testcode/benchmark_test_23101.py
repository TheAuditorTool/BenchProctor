# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
from types import SimpleNamespace


def BenchmarkTest23101(request):
    cookie_value = request.COOKIES.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        eval(str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
