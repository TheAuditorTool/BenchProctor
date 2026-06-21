# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import re
import asyncio


def BenchmarkTest48138(request):
    host_value = request.META.get('HTTP_HOST', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return host_value
    data = asyncio.run(fetch_payload())
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    digest = hashlib.md5(str(processed).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
