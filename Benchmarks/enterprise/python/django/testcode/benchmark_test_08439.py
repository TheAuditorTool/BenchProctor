# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import asyncio


def BenchmarkTest08439(request):
    user_id = request.GET.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = asyncio.run(fetch_payload())
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
