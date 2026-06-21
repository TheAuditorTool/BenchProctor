# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json


request_state: dict[str, str] = {}

async def BenchmarkTest60840(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    os.remove(str(data))
    return {"updated": True}
