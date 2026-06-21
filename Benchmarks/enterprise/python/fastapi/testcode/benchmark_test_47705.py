# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
import json
from starlette.responses import JSONResponse


async def BenchmarkTest47705(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
