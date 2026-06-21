# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import asyncio
from app_runtime import auth_check


def BenchmarkTest22011(request):
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = asyncio.run(fetch_payload())
    if not auth_check(request.session.get('user', ''), str(data)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
