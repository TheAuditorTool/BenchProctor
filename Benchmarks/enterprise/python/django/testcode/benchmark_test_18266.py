# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
from lxml import etree


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest18266(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = handle(referer_value)
    async def _evasion_task():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
