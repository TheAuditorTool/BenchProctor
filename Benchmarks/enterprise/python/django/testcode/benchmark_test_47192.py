# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import asyncio


def BenchmarkTest47192(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = asyncio.run(fetch_payload())
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
