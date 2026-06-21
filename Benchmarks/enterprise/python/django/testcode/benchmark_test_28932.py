# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import time
import asyncio


def BenchmarkTest28932(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        return HttpResponse(Template(data).render(Context()))
    return JsonResponse({"saved": True})
