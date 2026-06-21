# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os
import asyncio
from app_runtime import db


def BenchmarkTest55004(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = asyncio.run(fetch_payload())
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
