# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse
import json


def normalise_input(value):
    return value.strip()

async def BenchmarkTest37506(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = normalise_input(graphql_var)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
