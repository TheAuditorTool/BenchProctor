# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
import tempfile
from app_runtime import db


def BenchmarkTest08926(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = asyncio.run(fetch_payload())
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
