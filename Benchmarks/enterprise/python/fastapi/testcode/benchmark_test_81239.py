# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest81239(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    os.remove(str(data))
    return {"updated": True}
