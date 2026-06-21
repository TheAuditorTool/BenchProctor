# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest42317(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
