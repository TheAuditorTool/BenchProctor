# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import json


request_state: dict[str, str] = {}

async def BenchmarkTest80624(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
