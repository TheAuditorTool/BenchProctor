# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
import base64
from starlette.responses import JSONResponse


async def BenchmarkTest62376(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    eval(str(processed))
    return {"updated": True}
