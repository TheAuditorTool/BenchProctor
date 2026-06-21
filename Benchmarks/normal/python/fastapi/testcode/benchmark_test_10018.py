# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest10018(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
