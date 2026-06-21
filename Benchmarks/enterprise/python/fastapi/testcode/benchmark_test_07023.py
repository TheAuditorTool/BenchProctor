# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
import base64
from starlette.responses import JSONResponse


async def BenchmarkTest07023(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JSONResponse({'token': str(token)}, status_code=200)
