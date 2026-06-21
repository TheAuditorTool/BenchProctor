# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import asyncio
from app_runtime import db


def BenchmarkTest30533(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = asyncio.run(fetch_payload())
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})
