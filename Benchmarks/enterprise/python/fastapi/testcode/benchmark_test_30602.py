# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest30602(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JSONResponse({'token': str(token)}, status_code=200)
