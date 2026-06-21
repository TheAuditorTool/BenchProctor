# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import asyncio


def BenchmarkTest60432(request):
    xml_value = request.body.decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = asyncio.run(fetch_payload())
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
