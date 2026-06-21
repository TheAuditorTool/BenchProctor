# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from urllib.parse import unquote
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest80658(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
