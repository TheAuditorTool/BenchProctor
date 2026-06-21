# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest17544(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    ctx = RequestContext(xml_value)
    data = ctx.payload
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
