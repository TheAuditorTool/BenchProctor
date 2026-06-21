# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time
import asyncio
from app_runtime import db


def BenchmarkTest51456(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return ua_value
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return JsonResponse({"saved": True})
