# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
import asyncio


def BenchmarkTest00391(request):
    xml_value = request.body.decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = asyncio.run(fetch_payload())
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
