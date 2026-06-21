# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import os
import ast


async def BenchmarkTest27841(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    try:
        data = str(ast.literal_eval(xml_value))
    except (ValueError, SyntaxError):
        data = xml_value
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
