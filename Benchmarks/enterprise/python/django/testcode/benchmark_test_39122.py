# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import re
import asyncio


def BenchmarkTest39122(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = asyncio.run(fetch_payload())
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!()\\[\\]{}$-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    yaml.load(processed, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
