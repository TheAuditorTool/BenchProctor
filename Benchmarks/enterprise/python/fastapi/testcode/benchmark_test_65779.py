# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import defusedxml.ElementTree


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest65779(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
