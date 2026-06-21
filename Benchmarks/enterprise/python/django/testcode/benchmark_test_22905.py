# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import asyncio
import tempfile


def BenchmarkTest22905(request):
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = asyncio.run(fetch_payload())
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
