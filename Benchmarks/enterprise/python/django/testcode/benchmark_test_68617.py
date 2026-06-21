# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import asyncio


def BenchmarkTest68617(request):
    multipart_value = request.POST.get('multipart_field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return multipart_value
    data = asyncio.run(fetch_payload())
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
