# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from fastapi import Form
from starlette.responses import JSONResponse


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest42379(request: Request, field: str = Form('')):
    field_value = field
    data = coalesce_blank(field_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
