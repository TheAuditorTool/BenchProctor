# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest32774(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
