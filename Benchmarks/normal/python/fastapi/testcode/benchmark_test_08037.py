# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse
import ast


async def BenchmarkTest08037(request: Request):
    host_value = request.headers.get('host', '')
    try:
        data = str(ast.literal_eval(host_value))
    except (ValueError, SyntaxError):
        data = host_value
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
