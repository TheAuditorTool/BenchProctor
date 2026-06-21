# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
import base64
from starlette.responses import JSONResponse


async def BenchmarkTest62208(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JSONResponse({'token': str(token)}, status_code=200)
