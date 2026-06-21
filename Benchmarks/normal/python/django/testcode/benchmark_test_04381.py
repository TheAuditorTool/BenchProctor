# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import asyncio


def BenchmarkTest04381(request):
    cookie_value = request.COOKIES.get('session_token', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return cookie_value
    data = asyncio.run(fetch_payload())
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
