# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import asyncio
from app_runtime import auth_check


def BenchmarkTest66776(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = asyncio.run(fetch_payload())
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
