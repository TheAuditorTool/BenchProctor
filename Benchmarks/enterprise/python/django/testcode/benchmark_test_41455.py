# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


def coalesce_blank(value):
    return value or ''

def BenchmarkTest41455(request):
    raw_body = request.body.decode('utf-8')
    data = coalesce_blank(raw_body)
    async def _evasion_task():
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
