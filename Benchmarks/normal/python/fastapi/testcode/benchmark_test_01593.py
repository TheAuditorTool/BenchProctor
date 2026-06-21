# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest01593(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
