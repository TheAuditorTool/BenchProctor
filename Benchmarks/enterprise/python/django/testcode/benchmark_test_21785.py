# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os
import asyncio


def BenchmarkTest21785(request):
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = asyncio.run(fetch_payload())
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
