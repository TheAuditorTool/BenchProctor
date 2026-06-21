# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import re
from starlette.responses import JSONResponse
import ast


async def BenchmarkTest64409(request: Request):
    host_value = request.headers.get('host', '')
    try:
        data = str(ast.literal_eval(host_value))
    except (ValueError, SyntaxError):
        data = host_value
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    globals()['counter'] = int(processed)
    return {"updated": True}
