# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest03017(request: Request):
    host_value = request.headers.get('host', '')
    data = default_blank(host_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
