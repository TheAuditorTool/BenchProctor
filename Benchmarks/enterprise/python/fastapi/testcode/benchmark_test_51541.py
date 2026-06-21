# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
from starlette.responses import JSONResponse
import re


async def BenchmarkTest51541(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JSONResponse({'validated': str(data)}, status_code=200)
    return {"updated": True}
