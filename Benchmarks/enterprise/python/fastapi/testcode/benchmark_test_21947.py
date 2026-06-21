# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os
import ast


async def BenchmarkTest21947(request: Request):
    origin_value = request.headers.get('origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
