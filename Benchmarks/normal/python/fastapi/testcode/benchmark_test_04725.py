# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from fastapi import Form
from starlette.responses import JSONResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest04725(request: Request, field: str = Form('')):
    field_value = field
    data = ensure_str(field_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
