# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
from app_runtime import db


def BenchmarkTest66390(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return profile_value
    data = asyncio.run(fetch_payload())
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
