# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import asyncio


def BenchmarkTest54294(request):
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = asyncio.run(fetch_payload())
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
