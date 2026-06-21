# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import time
import asyncio


def BenchmarkTest27963(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        return HttpResponse(Template(data).render(Context()))
    return JsonResponse({"saved": True})
