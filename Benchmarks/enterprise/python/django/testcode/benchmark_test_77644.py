# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import asyncio
from app_runtime import auth_check


def BenchmarkTest77644(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    auth_check('user', data)
    return JsonResponse({"saved": True})
