# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import asyncio
from types import SimpleNamespace


def BenchmarkTest62280(request):
    xml_value = request.body.decode('utf-8')
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        yaml.load(data, Loader=yaml.UnsafeLoader)
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
