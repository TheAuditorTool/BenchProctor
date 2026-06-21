# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest49481(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = default_blank(ua_value)
    async def _evasion_task():
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
