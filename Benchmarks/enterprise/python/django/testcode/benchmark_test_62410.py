# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import asyncio
from types import SimpleNamespace


def BenchmarkTest62410(request):
    user_id = request.GET.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        _resp = requests.get(str(data))
        exec(_resp.text)
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
