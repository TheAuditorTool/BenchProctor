# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
from app_runtime import auth_check


def BenchmarkTest10991(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    async def fetch_payload():
        await asyncio.sleep(0)
        return secret_value
    data = asyncio.run(fetch_payload())
    auth_check('user', data)
    return JsonResponse({"saved": True})
