# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


async def BenchmarkTest75703(request: Request):
    origin_value = request.headers.get('origin', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(origin_value)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = origin_value
    return HTMLResponse(str(processed))
