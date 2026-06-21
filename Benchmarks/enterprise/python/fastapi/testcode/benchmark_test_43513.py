# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import ast
import ctypes


async def BenchmarkTest43513(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    try:
        data = str(ast.literal_eval(forwarded_ip))
    except (ValueError, SyntaxError):
        data = forwarded_ip
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JSONResponse({'wrapped': wrapped}, status_code=200)
