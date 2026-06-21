# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import ast


async def BenchmarkTest73620(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(data)})
