# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import asyncio


request_state: dict[str, str] = {}

def BenchmarkTest13910(request):
    user_id = request.GET.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    async def _evasion_task():
        return HttpResponse(Template(data).render(Context()))
    return asyncio.run(_evasion_task())
