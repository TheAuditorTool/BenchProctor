# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from fastapi import Form
from starlette.responses import JSONResponse
import ast


async def BenchmarkTest71026(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JSONResponse({'token': str(token)}, status_code=200)
