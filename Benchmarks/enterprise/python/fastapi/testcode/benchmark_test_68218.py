# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import time


request_state: dict[str, str] = {}

async def BenchmarkTest68218(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    if time.time() > 1000000000:
        eval(str(data))
    return {"updated": True}
