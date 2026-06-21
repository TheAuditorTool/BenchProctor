# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import asyncio
from types import SimpleNamespace
import subprocess


def BenchmarkTest59868(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        subprocess.run([str(data), '--status'], shell=False)
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
