# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest35851(request: Request):
    referer_value = request.headers.get('referer', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    processed = data[:64]
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return {"updated": True}
