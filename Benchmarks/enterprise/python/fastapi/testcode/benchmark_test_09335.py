# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import re
from starlette.responses import JSONResponse
import ast


async def BenchmarkTest09335(request: Request):
    host_value = request.headers.get('host', '')
    try:
        data = str(ast.literal_eval(host_value))
    except (ValueError, SyntaxError):
        data = host_value
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    return HTMLResponse('<div>' + str(processed) + '</div>')
