# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


async def BenchmarkTest18041(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', cookie_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = cookie_value
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return JSONResponse({'validated': str(processed)}, status_code=200)
    return {"updated": True}
