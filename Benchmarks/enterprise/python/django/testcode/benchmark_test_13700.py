# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
from types import SimpleNamespace


def BenchmarkTest13700(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        with open('/var/app/data/' + str(data), 'w') as fh:
            fh.write('data')
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
