# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest02474(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
