# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest77418(request: Request):
    path_value = request.path_params.get('id', '')
    ctx = RequestContext(path_value)
    data = ctx.payload
    eval(compile('_parser = etree.XMLParser(resolve_entities=True, no_network=False)\netree.fromstring(str(data).encode(), _parser)', '<sink>', 'exec'))
    return {"updated": True}
