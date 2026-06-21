# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


def BenchmarkTest37195(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = asyncio.run(fetch_payload())
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
