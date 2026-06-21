# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form
import os
import ast


async def BenchmarkTest35237(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
