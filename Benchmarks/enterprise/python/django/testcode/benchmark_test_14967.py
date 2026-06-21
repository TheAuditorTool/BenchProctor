# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
from app_runtime import db


def BenchmarkTest14967(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return profile_value
    data = asyncio.run(fetch_payload())
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
