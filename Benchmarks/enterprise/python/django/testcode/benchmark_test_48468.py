# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import asyncio
from app_runtime import db


def BenchmarkTest48468(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = asyncio.run(fetch_payload())
    async def _evasion_task():
        return redirect(str(data))
    return asyncio.run(_evasion_task())
