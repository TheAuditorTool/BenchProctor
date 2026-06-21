# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time
import asyncio


def BenchmarkTest34462(request):
    xml_value = request.body.decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    return JsonResponse({"saved": True})
