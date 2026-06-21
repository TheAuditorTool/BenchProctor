# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest12607(request: Request, field: str = Form('')):
    field_value = field
    data, _sep, _rest = str(field_value).partition('\x00')
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
