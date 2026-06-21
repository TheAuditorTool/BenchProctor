# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse
import json


request_state: dict[str, str] = {}

async def BenchmarkTest16234(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
