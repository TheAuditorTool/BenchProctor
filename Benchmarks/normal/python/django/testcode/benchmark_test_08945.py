# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json
import asyncio


def BenchmarkTest08945(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
