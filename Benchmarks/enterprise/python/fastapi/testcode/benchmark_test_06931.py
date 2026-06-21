# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json


request_state: dict[str, str] = {}

async def BenchmarkTest06931(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
