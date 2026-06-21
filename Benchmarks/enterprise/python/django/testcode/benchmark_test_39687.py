# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import asyncio
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest39687(request):
    raw_body = request.body.decode('utf-8')
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    async def _evasion_task():
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
