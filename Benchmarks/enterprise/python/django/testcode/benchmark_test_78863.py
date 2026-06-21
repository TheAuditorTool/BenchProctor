# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import asyncio
from types import SimpleNamespace


def BenchmarkTest78863(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
