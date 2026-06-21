# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import asyncio
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest58717(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ctx = RequestContext(db_value)
    data = ctx.payload
    async def _evasion_task():
        requests.get(str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
