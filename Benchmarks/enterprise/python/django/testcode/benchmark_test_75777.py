# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
from lxml import etree


request_state: dict[str, str] = {}

def BenchmarkTest75777(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    async def _evasion_task():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
