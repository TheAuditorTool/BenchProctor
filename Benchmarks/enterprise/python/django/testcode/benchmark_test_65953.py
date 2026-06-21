# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


def coalesce_blank(value):
    return value or ''

def BenchmarkTest65953(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = coalesce_blank(forwarded_ip)
    async def _evasion_task():
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
