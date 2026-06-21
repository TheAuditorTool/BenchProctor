# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest74093(request):
    upload_name = request.FILES['upload'].name
    data = default_blank(upload_name)
    async def _evasion_task():
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
