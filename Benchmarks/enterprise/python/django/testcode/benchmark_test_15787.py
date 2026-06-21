# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
import asyncio


def BenchmarkTest15787(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + data
    os.unlink(checked_path)
    return JsonResponse({"saved": True})
