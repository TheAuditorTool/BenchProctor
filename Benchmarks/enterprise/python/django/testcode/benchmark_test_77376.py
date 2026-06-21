# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


def normalise_input(value):
    return value.strip()

def BenchmarkTest77376(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = normalise_input(multipart_value)
    async def _evasion_task():
        eval(str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
