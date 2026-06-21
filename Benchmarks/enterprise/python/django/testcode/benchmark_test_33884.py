# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


def BenchmarkTest33884(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = asyncio.run(fetch_payload())
    if str(data).lower() not in ('true', 'false'):
        return JsonResponse({'error': 'invalid boolean'}, status=400)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
