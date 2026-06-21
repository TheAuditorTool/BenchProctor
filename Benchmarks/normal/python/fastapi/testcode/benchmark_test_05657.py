# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import os
import time


request_state: dict[str, str] = {}

async def BenchmarkTest05657(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    if time.time() > 1000000000:
        link_path = os.path.join('/var/app/data', str(data))
        target = os.readlink(link_path)
        with open(target, 'r') as fh:
            content = fh.read()
        return content
    return {"updated": True}
