# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from fastapi import Form
from starlette.responses import JSONResponse
import ast


async def BenchmarkTest34453(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
