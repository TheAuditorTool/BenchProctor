# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


def BenchmarkTest77348(request, path_param):
    path_value = path_param
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
