# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
from app_runtime import auth_check


def BenchmarkTest31386(request):
    cookie_value = request.COOKIES.get('session_token', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return cookie_value
    data = asyncio.run(fetch_payload())
    if auth_check('user', str(data)):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
