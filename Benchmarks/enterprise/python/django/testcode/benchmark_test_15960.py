# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


def BenchmarkTest15960(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return ua_value
    data = asyncio.run(fetch_payload())
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
