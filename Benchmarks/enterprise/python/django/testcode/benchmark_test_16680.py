# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import asyncio


def BenchmarkTest16680(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = asyncio.run(fetch_payload())
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
