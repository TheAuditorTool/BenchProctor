# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest37648(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
