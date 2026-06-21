# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


def BenchmarkTest44080(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = asyncio.run(fetch_payload())
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
