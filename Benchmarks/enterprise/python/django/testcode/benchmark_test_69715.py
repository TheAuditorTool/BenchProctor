# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import os
import asyncio


def BenchmarkTest69715(request):
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = asyncio.run(fetch_payload())
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
