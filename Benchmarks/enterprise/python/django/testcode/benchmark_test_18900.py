# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import asyncio


def BenchmarkTest18900(request):
    user_id = request.GET.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = asyncio.run(fetch_payload())
    async def _evasion_task():
        return HttpResponse(Template(data).render(Context()))
    return asyncio.run(_evasion_task())
