# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import html
import os
import asyncio


def BenchmarkTest10117(request):
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = asyncio.run(fetch_payload())
    processed = str(data).replace("<script", "")
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
