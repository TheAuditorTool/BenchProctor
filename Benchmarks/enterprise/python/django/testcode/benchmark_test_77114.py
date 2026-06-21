# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time
import asyncio
import runpy


def BenchmarkTest77114(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    return JsonResponse({"saved": True})
