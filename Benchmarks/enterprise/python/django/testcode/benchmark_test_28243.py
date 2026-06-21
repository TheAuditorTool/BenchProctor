# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
from app_runtime import auth_check


def BenchmarkTest28243(request):
    user_id = request.GET.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = asyncio.run(fetch_payload())
    if not auth_check(request.session.get('user', ''), str(data)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
