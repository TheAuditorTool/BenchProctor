# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import asyncio
from app_runtime import db


def BenchmarkTest05023(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return profile_value
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    os.unlink('/var/app/data/' + str(processed))
    return JsonResponse({"saved": True})
