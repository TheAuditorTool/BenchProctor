# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
from app_runtime import db, auth_check


def BenchmarkTest01920(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = asyncio.run(fetch_payload())
    if not auth_check(request.session.get('user', ''), str(data)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
