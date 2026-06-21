# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import time


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest19071(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    if time.time() > 1000000000:
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return {"updated": True}
