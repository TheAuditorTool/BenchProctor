# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import asyncio


def BenchmarkTest73205(request):
    xml_value = request.body.decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = asyncio.run(fetch_payload())
    async def _evasion_task():
        os.system('echo ' + str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
