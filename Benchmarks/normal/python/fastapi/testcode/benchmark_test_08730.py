# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest08730(request: Request, field: str = Form('')):
    field_value = field
    if field_value:
        data = field_value
    else:
        data = ''
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
