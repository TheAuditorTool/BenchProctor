# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import asyncio


def BenchmarkTest04233(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return ua_value
    data = asyncio.run(fetch_payload())
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
