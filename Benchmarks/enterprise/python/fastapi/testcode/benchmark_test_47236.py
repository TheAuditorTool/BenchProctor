# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import ast


async def BenchmarkTest47236(request: Request):
    upload_name = (await request.form()).get('upload', '')
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
