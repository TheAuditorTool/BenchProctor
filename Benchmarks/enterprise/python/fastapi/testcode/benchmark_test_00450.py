# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


request_state: dict[str, str] = {}

async def BenchmarkTest00450(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
