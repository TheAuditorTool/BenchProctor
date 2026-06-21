# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
from app_runtime import auth_check


def BenchmarkTest38025(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    async def fetch_payload():
        await asyncio.sleep(0)
        return prop_value
    data = asyncio.run(fetch_payload())
    auth_check('user', data)
    return JsonResponse({"saved": True})
