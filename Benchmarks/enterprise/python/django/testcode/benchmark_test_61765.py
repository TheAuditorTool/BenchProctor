# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import asyncio
from types import SimpleNamespace


def BenchmarkTest61765(request):
    upload_name = request.FILES['upload'].name
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        subprocess.run('echo ' + str(data), shell=True)
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
