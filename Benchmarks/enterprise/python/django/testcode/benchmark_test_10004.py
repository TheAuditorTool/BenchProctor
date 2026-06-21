# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
from app_runtime import db


def BenchmarkTest10004(request):
    xml_value = request.body.decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = asyncio.run(fetch_payload())
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return JsonResponse({"saved": True})
