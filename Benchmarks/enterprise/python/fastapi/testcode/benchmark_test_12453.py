# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import ast


async def BenchmarkTest12453(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
