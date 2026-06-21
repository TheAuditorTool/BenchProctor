# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
from types import SimpleNamespace
from lxml import etree


def BenchmarkTest42099(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
