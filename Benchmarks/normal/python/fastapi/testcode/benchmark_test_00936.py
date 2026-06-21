# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest00936(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return JSONResponse({'token': str(token)}, status_code=200)
