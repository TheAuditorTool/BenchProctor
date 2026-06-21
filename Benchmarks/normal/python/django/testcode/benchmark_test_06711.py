# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import os
import asyncio
import pickle


def BenchmarkTest06711(request):
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = asyncio.run(fetch_payload())
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!()\\[\\]{}$-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    pickle.loads(processed.encode('latin-1'))
    return JsonResponse({"saved": True})
