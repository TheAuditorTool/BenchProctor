# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
import importlib
import sys


def coalesce_blank(value):
    return value or ''

def BenchmarkTest54835(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = coalesce_blank(ua_value)
    async def _evasion_task():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
