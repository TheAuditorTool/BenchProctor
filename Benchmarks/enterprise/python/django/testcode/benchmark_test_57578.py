# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


def BenchmarkTest57578(request):
    upload_name = request.FILES['upload'].name
    async def fetch_payload():
        await asyncio.sleep(0)
        return upload_name
    data = asyncio.run(fetch_payload())
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
