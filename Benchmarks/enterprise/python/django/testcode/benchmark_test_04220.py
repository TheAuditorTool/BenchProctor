# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import asyncio
from types import SimpleNamespace


def BenchmarkTest04220(request, path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        requests.get(str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
