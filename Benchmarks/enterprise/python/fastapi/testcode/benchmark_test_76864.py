# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest76864(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    ctx = RequestContext(forwarded_ip)
    data = ctx.payload
    yaml.safe_load(data)
    return {"updated": True}
