# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import time
import asyncio
from app_runtime import db


def BenchmarkTest01410(request):
    xml_value = request.body.decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return JsonResponse({"saved": True})
