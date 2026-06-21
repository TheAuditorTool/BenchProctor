# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


async def BenchmarkTest28755(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', cookie_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = cookie_value
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(processed)})
