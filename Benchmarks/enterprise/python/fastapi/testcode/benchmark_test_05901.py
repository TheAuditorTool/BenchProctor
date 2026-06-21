# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from lxml import etree


class UserInput(BaseModel):
    payload: str = ''
class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest05901(request: Request, req: UserInput):
    json_value = req.payload
    ctx = RequestContext(json_value)
    data = ctx.payload
    processed = data[:64]
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return {"updated": True}
