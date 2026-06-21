# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest04484(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    ctx = RequestContext(xml_value)
    data = ctx.payload
    def _primary():
        eval(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
