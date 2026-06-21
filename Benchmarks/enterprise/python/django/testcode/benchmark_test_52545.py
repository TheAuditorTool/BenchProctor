# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import asyncio
import requests


def BenchmarkTest52545(request):
    host_value = request.META.get('HTTP_HOST', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return host_value
    data = asyncio.run(fetch_payload())
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
