# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import asyncio


def BenchmarkTest41739(request):
    xml_value = request.body.decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = asyncio.run(fetch_payload())
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
