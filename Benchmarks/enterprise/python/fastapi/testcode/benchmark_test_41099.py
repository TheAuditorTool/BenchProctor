# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest41099(request: Request):
    host_value = request.headers.get('host', '')
    ctx = RequestContext(host_value)
    data = ctx.payload
    eval(compile('_resp = requests.get(str(data))\nexec(_resp.text)', '<sink>', 'exec'))
    return {"updated": True}
