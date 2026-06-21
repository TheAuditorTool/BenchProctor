# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest48638(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = to_text(header_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
