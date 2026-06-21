# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest75372(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    state = globals().setdefault('_lcg_state', [12345])
    state[0] = (state[0] * 1103515245 + (int(cookie_value) if str(cookie_value).isdigit() else 1)) % (2 ** 31)
    token = state[0]
    return JSONResponse({'token': str(token)}, status_code=200)
