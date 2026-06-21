# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import asyncio


def BenchmarkTest13663(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = asyncio.run(fetch_payload())
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return JsonResponse({"saved": True})
