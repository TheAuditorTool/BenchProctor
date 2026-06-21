# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest02147(request: Request):
    origin_value = request.headers.get('origin', '')
    ctx = RequestContext(origin_value)
    data = ctx.payload
    yaml.safe_load(data)
    return {"updated": True}
