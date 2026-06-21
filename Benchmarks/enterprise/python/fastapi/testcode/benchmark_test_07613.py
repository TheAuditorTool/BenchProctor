# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest07613(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value}'
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
