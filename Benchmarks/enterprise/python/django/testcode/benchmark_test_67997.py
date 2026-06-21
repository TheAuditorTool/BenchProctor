# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
from types import SimpleNamespace


def BenchmarkTest67997(request):
    raw_body = request.body.decode('utf-8')
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        eval(str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
