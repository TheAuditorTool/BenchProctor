# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import asyncio


def BenchmarkTest00991(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = asyncio.run(fetch_payload())
    checked_path = os.path.normpath(data)
    with open('/var/uploads/' + str(checked_path), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
