# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest21197(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    async def _evasion_task():
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return content
    return await _evasion_task()
