# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest79592(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    arr = [10, 20, 30, 40, 50]
    idx = int(str(cookie_value))
    return JSONResponse({'lookup': arr[idx]}, status_code=200)
