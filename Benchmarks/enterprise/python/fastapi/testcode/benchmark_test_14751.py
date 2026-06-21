# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest14751(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = ensure_str(header_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
