# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


async def BenchmarkTest08244(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(header_value)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = header_value
    return HTMLResponse(str(processed))
