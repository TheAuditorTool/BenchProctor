# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


def BenchmarkTest09141(request):
    upload_name = request.FILES['upload'].name
    async def fetch_payload():
        await asyncio.sleep(0)
        return upload_name
    data = asyncio.run(fetch_payload())
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
