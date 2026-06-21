# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest31077(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        os.system('echo ' + str(data))
    return {"updated": True}
