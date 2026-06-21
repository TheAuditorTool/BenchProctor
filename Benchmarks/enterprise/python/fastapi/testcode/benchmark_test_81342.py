# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest81342(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = normalise_input(ua_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
