# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import ast


async def BenchmarkTest00422(request: Request):
    referer_value = request.headers.get('referer', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
