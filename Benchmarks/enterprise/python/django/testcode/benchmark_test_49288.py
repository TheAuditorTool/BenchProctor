# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import asyncio


request_state: dict[str, str] = {}

def BenchmarkTest49288(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    async def _evasion_task():
        return HttpResponse(Template(data).render(Context()))
    return asyncio.run(_evasion_task())
