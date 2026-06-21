# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import asyncio
import subprocess


def BenchmarkTest63105(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = asyncio.run(fetch_payload())
    async def _evasion_task():
        subprocess.run([str(data), '--status'], shell=False)
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
