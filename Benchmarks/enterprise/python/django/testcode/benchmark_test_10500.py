# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
from lxml import etree


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest10500(request):
    upload_name = request.FILES['upload'].name
    ctx = RequestContext(upload_name)
    data = ctx.payload
    async def _evasion_task():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
