# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
import defusedxml.ElementTree


def BenchmarkTest63943(request):
    user_id = request.GET.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = asyncio.run(fetch_payload())
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
