# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
from lxml import etree


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest57196():
    header_value = request.headers.get('X-Custom-Header', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    async def _evasion_task():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
