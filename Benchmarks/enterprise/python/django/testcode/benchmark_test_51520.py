# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
from lxml import etree
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest51520(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ctx = RequestContext(db_value)
    data = ctx.payload
    async def _evasion_task():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
