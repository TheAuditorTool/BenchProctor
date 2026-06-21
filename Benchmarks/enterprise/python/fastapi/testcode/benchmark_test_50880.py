# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest50880(request: Request):
    host_value = request.headers.get('host', '')
    data = normalise_input(host_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
