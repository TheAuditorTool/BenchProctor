# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from fastapi import Form
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest27116(request: Request, field: str = Form('')):
    field_value = field
    data = to_text(field_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
