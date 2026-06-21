# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
import asyncio


def BenchmarkTest18830(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = asyncio.run(fetch_payload())
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
