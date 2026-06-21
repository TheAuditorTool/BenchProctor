# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
from app_runtime import db


def BenchmarkTest30245(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = asyncio.run(fetch_payload())
    async def _evasion_task():
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
