# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
import socket


def BenchmarkTest59667(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = asyncio.run(fetch_payload())
    def _primary():
        s = socket.create_connection((str(data), 80))
        s.close()
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
