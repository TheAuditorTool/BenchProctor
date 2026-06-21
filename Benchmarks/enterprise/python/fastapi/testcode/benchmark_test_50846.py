# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest50846(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    random.seed(int(cookie_value) if str(cookie_value).isdigit() else 42)
    token = str(random.random())
    return JSONResponse({'token': str(token)}, status_code=200)
