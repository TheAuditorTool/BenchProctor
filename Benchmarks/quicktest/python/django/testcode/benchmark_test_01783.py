# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import asyncio
import defusedxml.ElementTree


def BenchmarkTest01783(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
