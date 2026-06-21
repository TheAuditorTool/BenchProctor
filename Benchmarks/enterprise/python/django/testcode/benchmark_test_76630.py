# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import asyncio


def BenchmarkTest76630(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
