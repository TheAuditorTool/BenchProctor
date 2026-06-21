# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os
import asyncio
from app_runtime import db


def BenchmarkTest62724(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = asyncio.run(fetch_payload())
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
