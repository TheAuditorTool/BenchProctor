# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


def coalesce_blank(value):
    return value or ''

def BenchmarkTest30397(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = coalesce_blank(multipart_value)
    async def _evasion_task():
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
