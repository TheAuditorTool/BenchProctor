# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import ast


async def BenchmarkTest05913(request: Request):
    upload_name = (await request.form()).get('upload', '')
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
