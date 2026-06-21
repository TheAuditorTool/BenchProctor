# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time
import asyncio
from app_runtime import db


def BenchmarkTest57709(request):
    upload_name = request.FILES['upload'].name
    async def fetch_payload():
        await asyncio.sleep(0)
        return upload_name
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return JsonResponse({"saved": True})
