# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
import importlib
import sys
from types import SimpleNamespace


def BenchmarkTest59353(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
