# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from lxml import etree


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest20476(request: Request):
    path_value = request.path_params.get('id', '')
    ctx = RequestContext(path_value)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
