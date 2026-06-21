# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest03055(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
