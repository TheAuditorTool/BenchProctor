# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
from lxml import etree


def BenchmarkTest66410(request):
    raw_body = request.body.decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(raw_body)
    data = collected
    async def _evasion_task():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
