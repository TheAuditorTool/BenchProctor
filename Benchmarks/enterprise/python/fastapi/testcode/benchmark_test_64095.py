# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest64095(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
