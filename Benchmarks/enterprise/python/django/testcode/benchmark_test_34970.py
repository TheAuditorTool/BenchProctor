# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import time
import asyncio


def BenchmarkTest34970(request):
    user_id = request.GET.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
    return JsonResponse({"saved": True})
