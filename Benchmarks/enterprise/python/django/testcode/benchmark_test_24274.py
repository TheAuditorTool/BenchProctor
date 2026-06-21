# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import os
import asyncio


def BenchmarkTest24274(request):
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = asyncio.run(fetch_payload())
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(processed))
    return resp
