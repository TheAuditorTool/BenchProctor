# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import asyncio
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest79999(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    async def _evasion_task():
        os.system('echo ' + str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
