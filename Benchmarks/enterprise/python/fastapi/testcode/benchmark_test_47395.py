# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


async def BenchmarkTest47395(request: Request):
    host_value = request.headers.get('host', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(host_value)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = host_value
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
